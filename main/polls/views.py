from django.shortcuts import render
from rest_framework import viewsets

from polls import models
from . import serializers

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class OptionViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = models.Option.objects.all()
    serializer_class = serializers.OptionSerializer


class PollViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer


class VoteViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, ]
        if self.request.method == 'POST':
            self.permission_classes = []

        return super(VoteViewSet, self).get_permissions()
