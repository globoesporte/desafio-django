from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from api.models import Enquete, Item, Voto
from rest_framework import viewsets, mixins, generics, status
from api.serializer import UserSerializer, GroupSerializer, EnqueteSerializer, ItemSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
import logging


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

class EnqueteEditView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, pk, *args, **kwargs):
        return Response({'pk' : pk}, template_name = 'enquete_edit.html')

class EnqueteListView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        return Response(template_name = 'enquete_list.html')

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

class ItemEditView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, pk, *args, **kwargs):
        id_enquete = self.request.query_params.get('enquete', None)
        return Response({'id_enquete' : id_enquete, 'pk' : pk}, template_name = 'item_edit.html')

class ItemListView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        id_enquete = self.request.query_params.get('enquete', None)
        return Response({'id_enquete' : id_enquete}, template_name = 'item_list.html')

class ItemNewView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        id_enquete = self.request.query_params.get('enquete', None)
        return Response({'id_enquete' : id_enquete}, template_name = 'item_new.html')
    

