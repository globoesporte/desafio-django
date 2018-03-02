from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from api.models import Enquete, Item, Voto
from rest_framework import viewsets, mixins, generics, status
from api.serializer import UserSerializer, GroupSerializer, EnqueteSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes


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

# class EnqueteList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'enquete_list.html'
#     """
#     List all Enquetes, or create a new Enquete.
#     """
#     def get(self, request, format=None):
#         enquetes = Enquete.objects.all()
#         return Response({'profiles': enquetes})

#     def post(self, request, format=None):
#         serializer = EnqueteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EnqueteDetail(APIView):
#     # renderer_classes = [TemplateHTMLRenderer]
#     # template_name = 'enquete_detail.html'
    
#     def get_object(self, pk):
#         try:
#             return Enquete.objects.get(pk=pk)
#         except Enquete.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         enquete = self.get_object(pk)
#         serializer = EnqueteSerializer(enquete)
#         return Response(serializer.data)
#         # return Response({'serializer': serializer, 'profile': enquete})

#     def put(self, request, pk, format=None):
#         Enquete = self.get_object(pk)
#         serializer = EnqueteSerializer(Enquete, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             # return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#             return Response(serializer.data, content_type='application/json', status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         Enquete = self.get_object(pk)
#         Enquete.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

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
