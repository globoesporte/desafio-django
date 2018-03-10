from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Survey,Options
from .serializers import SurveySerializer,OptionsSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render
import sys

def SurveyList(request):
    surveys = Survey.objects.all()
    return render(request, 'surveys.html', {'surveys': surveys, })

class SurveyActs(APIView):
    """
    List all code surveys, or create a new survey.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        if pk:
            surveys = get_object_or_404(Survey, pk=pk)
            serializer = SurveySerializer(surveys)
        else:
            surveys = Survey.objects.all()
            serializer = SurveySerializer(surveys, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self,request, pk):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def put(self, request, pk): 
        survey=get_object_or_404(Survey, pk=pk)
        serializer = SurveySerializer(survey, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
    
    def delete(self, request, pk):
            surveys = get_object_or_404(Survey, pk=pk)
            surveys.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class OptionActs(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = OptionsSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return  JsonResponse(serializer.data, status=201)


    def put(self, request, survey,pk):
        option = get_object_or_404(Options,pk=pk)
        serializer = OptionsSerializer(option,data=request.data,
                                       context={'survey': survey}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return  JsonResponse(serializer.data, status=201)

    def delete(self,request,survey,pk):
        try:
            option = Options.objects.filter(pk=pk,survey__pk=survey).get()
            option.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except RuntimeError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class VoteActs(APIView):

    def post(self, request, survey,pk):
        try:
            option = Options.objects.filter(survey__pk=survey).get(pk=pk)
            option.vote(pk,1)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except RuntimeError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        option = get_object_or_404(Options,pk=pk)
        serializer = OptionsSerializer(option,data=request.data,
                                       context={'survey': survey}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return  JsonResponse(serializer.data, status=201)

    def delete(self,request,survey,pk):
        try:
            option = Options.objects.filter(survey__pk=survey).get(pk=pk)
            option.vote(pk,-1)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except RuntimeError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, survey, pkold, pk):
        try:
            option = Options.objects.filter(survey__pk=survey).get(pk=pkold)
            option.vote(pkold,-1)
            option = Options.objects.filter(survey__pk=survey).get(pk=pk)
            option.vote(pk,1)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except RuntimeError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



