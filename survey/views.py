from .models import Survey, Option
from .serializer import SurveySerializer, OptionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class SurveyList(APIView):
    serializerClass = SurveySerializer

    def get(self,request,format=None):
        """

        :param request:
        :param format:
        :return:
        """
        serializer = self.serializerClass(Survey.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """

        :param request:
        :param format:
        :return:
        """
        serializer = self.serializerClass(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class SurveyInfo(APIView):
    serializerClass = SurveySerializer

    def get(self, request, pk, format=None):
        """

        :param request:
        :param pk:
        :param format:
        :return:
        """
        serializer = self.serializerClass(Survey.objects.get(pk=pk))
        return Response(serializer.data)
