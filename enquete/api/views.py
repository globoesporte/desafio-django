from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from api.models import Enquete, Item, Voto
from rest_framework import viewsets, mixins, generics, status, permissions
from api.serializer import UserSerializer, GroupSerializer, EnqueteSerializer, ItemSerializer, VotoSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
import logging
from api.worker import VotoWorker
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic import RedirectView

def UserLogin(request):
    next_page = request.GET['next']
    if request.user.is_authenticated():
        return HttpResponseRedirect(next_page)
    else:
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(email=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(next_page)
                else:
                    error_msg = 'There was an error!'
                    return render(request, "login", {'form': form, 'error_msg': error_msg})
            else:
                error_msg = "There was an error!"
                return render(request, "login", {'form':form, 'error_msg':error_msg})
        else:
            form = UserLoginForm()
            return render(request, "login", {'form': form})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class EnqueteDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Enquete.objects.all()
    serializer_class = EnqueteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
 
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
 
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
 
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class EnqueteList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Enquete.objects.all()
    serializer_class = EnqueteSerializer
 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
 
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@method_decorator(login_required(login_url='/admin/login/?next=/enquete/all'), name='dispatch')
class EnqueteEditView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, pk, *args, **kwargs):
        return Response({'pk' : pk}, template_name = 'enquete_edit.html')

@method_decorator(login_required(login_url='/admin/login/?next=/enquete/all'), name='dispatch')
class EnqueteListView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        return Response(template_name = 'enquete_list.html')

@method_decorator(login_required(login_url='/admin/login/?next=/enquete/all'), name='dispatch')
class EnqueteNewView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        return Response(template_name = 'enquete_new.html')


class ItemDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
 
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
 
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
 
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ItemList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
 
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Item.objects.all()
        enquete = self.request.query_params.get('enquete', None)
        if enquete is not None:
            queryset = queryset.filter(enquete_id=enquete)
        return queryset    

@method_decorator(login_required(login_url='/admin/login/?next=/enquete/all'), name='dispatch')
class ItemEditView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, pk, *args, **kwargs):
        id_enquete = self.request.query_params.get('enquete', None)
        return Response({'id_enquete' : id_enquete, 'pk' : pk}, template_name = 'item_edit.html')

@method_decorator(login_required(login_url='/admin/login/?next=/enquete/all'), name='dispatch')
class ItemListView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        id_enquete = self.request.query_params.get('enquete', None)
        return Response({'id_enquete' : id_enquete}, template_name = 'item_list.html')

@method_decorator(login_required(login_url='/admin/login/?next=/enquete/all'), name='dispatch')
class ItemNewView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        id_enquete = self.request.query_params.get('enquete', None)
        return Response({'id_enquete' : id_enquete}, template_name = 'item_new.html')
    
class VotacaoView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        id_enquete = self.request.query_params.get('enquete', None)
        return Response({'id_enquete' : id_enquete}, template_name = 'votacao.html')

class VotarView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
 
    serializer_class = VotoSerializer
 
    def post(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        serializer = VotoSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            worker = VotoWorker()
            worker.adicionar_voto(validated_data)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
        


class RedirectToHome(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('/enquete/all')