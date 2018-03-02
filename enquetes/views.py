from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .models import Enquete, Resposta

# Implementando os ENDPOINTS REST
#
from rest_framework import viewsets, response, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import django_filters.rest_framework

from django.db.models import Sum

from .serializers import *
from .tasks import *


class IndexView(generic.ListView):
    template_name = 'enquetes/index.html'
    context_object_name = 'ultimas_enquetes'

    def get_queryset(self):
        return Enquete.objects.filter(ativa=True).annotate(
            votos=Sum('respostas__votos')
        )


def votar(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)

    try:
        resposta = request.POST['resposta']
        resposta_selecionada = enquete.respostas.get(
            pk=resposta)
    except (KeyError):

        messages.error(request, "Você não selecionou nenhuma das opções.")
        return HttpResponseRedirect(reverse('enquetes:index'))

    else:
        try:
            resposta = task_votar.delay(resposta_selecionada.id)

            messages.info(request, "Obrigado pelo voto!")
            return HttpResponseRedirect(reverse('enquetes:index'))

        except(Exception):
            messages.error(request, "Problemas ao computar seu voto!")
            return HttpResponseRedirect(reverse('enquetes:index'))

# REST


class EnqueteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Enquetes to be viewed or edited.
    """
    queryset = Enquete.objects.all()
    serializer_class = EnqueteSerializer


class RespostaViewSet(viewsets.ModelViewSet):
    """
    View used by Respostas API
    """
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class RespostasViewSet(viewsets.ModelViewSet):
    """
    View used by Respostas API
    """
    serializer_class = RespostaSerializer

    def get_queryset(self):
        return Enquete.objects.get(pk=self.kwargs['enquete_pk']).respostas

    def create(self, request, enquete_pk):

        serializer = RespostaSerializer(data=request.data,
                                        context={'enquete_pk': enquete_pk})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data,
                                 status=status.HTTP_201_CREATED,
                                 headers=headers)


class VotoViewSet(viewsets.GenericViewSet):

    permission_classes = [AllowAny]

    def create(self, request, resposta_pk):
        try:
            resposta = task_votar.delay(resposta_pk)

            # Votação assíncrona. Não tem mais como retornar os votos
            # data = {"votos": resposta.votos}
            headers = {}

            return response.Response({},
                                     status=status.HTTP_201_CREATED,
                                     headers=headers)
        except Exception as ex:
            return response.Response({},
                                     status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                     headers={})
