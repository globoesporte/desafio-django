from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from api.models import Enquete, Item, Voto
from rest_framework import viewsets, mixins
from api.serializer import UserSerializer, GroupSerializer, EnqueteSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


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

# class EnqueteViewSet(APIView):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Enquete.objects.all()
#     serializer_class = GroupSerializer
   
#     def get(self, request):
        

#         return Response(serializer.data)

class EnqueteList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'enquete_list.html'
    """
    List all Enquetes, or create a new Enquete.
    """
    def get(self, request, format=None):
        enquetes = Enquete.objects.all()
        return Response({'profiles': enquetes})

    def post(self, request, format=None):
        serializer = EnqueteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnqueteDetail(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'enquete_detail.html'
    
    def get_object(self, pk):
        try:
            return Enquete.objects.get(pk=pk)
        except Enquete.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        
        enquete = self.get_object(pk)
        serializer = EnqueteSerializer(enquete)
        return Response(serializer.data)
        # return Response({'serializer': serializer, 'profile': enquete})

    def put(self, request, pk):
        Enquete = self.get_object(pk)
        serializer = EnqueteSerializer(Enquete, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            # return redirect('enquete-list')
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Enquete = self.get_object(pk)
        Enquete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
