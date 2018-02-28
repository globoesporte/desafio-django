from .models import Survey, Option
from .serializer import SurveySerializer, OptionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class SurveyList(APIView):
    serializerClass = SurveySerializer

    def get(self,request,format=None):
        serializer = self.serializerClass(Survey.objects.all(), many=True)
        return Response(serializer.data)
