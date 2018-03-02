from django.shortcuts import render
from rest_framework import viewsets

from polls import models
from . import serializers


class OptionViewSet(viewsets.ModelViewSet):
	queryset = models.Option.objects.all()
	serializer_class = serializers.OptionSerializer


class PollViewSet(viewsets.ModelViewSet):
	queryset = models.Poll.objects.all()
	serializer_class = serializers.PollSerializer


class VoteViewSet(viewsets.ModelViewSet):
	queryset = models.Vote.objects.all()
	serializer_class = serializers.VoteSerializer
