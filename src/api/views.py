from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveAPIView, ListAPIView

from enqueteapp.permissions import IsOwnerOrReadOnly
from enqueteapp.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

from rest_framework import status

class AllQuestionsView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = QuestionSerializer

    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = QuestionSerializer

    def get_object(self, pk):
        return Question.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""
class AllChoicesView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ChoiceSerializer
    
    def get(self, request, format=None):
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChoiceView(APIView):
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ChoiceSerializer

    def get_object(self, pk):
        return Choice.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        choice = self.get_object(pk)
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        choice = self.get_object(pk)
        serializer = ChoiceSerializer(choice, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)

    
    def delete(self, request, pk, format=None):
        choice= self.get_object(pk)
        choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VoteView(APIView):

    def get_object(self, pk):
        return Choice.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        choice = self.get_object(pk=pk)
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        choice = self.get_object(pk=pk)
        choice.add_vote()
        return Response(status = status.HTTP_201_CREATED)

