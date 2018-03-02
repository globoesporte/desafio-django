from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from rest_framework.test import APIClient

from requests.auth import HTTPBasicAuth


from .test_util import *

from .test_base import *


class BaseRESTDeveTests(TestCase):
    URL_ENQUETE = 'http://localhost:8000/enquetes/api/enquete/'
    URL_RESPOSTA = 'http://localhost:8000/enquetes/api/resposta/'

    body = {"texto":
            "Qual a velocidade de uma andorinha?",
            "ativa": True,
            "respostas": [
                {"id": 1000, "opcao":
                 "Andorinhas europeias?"},
                {"opcao": "Andorinhas africanas?"},
                {"opcao": "Ahhhhrg!"}
            ]
            }

    bodyRetorno = {
        "id": 1,
        "texto":
            "Qual a velocidade de uma andorinha?",
            "ativa": True,
            "respostas": [
                {"id": 1, "opcao":
                 "Andorinhas europeias?", "votos": 0},
                {"id": 2, "opcao": "Andorinhas africanas?", "votos": 0},
                {"id": 3, "opcao": "Ahhhhrg!", "votos": 0}
            ]
    }

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user(
            'testuser', email='testuser@test.com', password='testing')
        self.user.save()

    def criaEnquete(self):
        response = self.client.post(
            self.URL_ENQUETE,
            self.body, format='json')

        return response

    def criaResposta(self):
        resposta = {"id": 4, "opcao": "ek ek ek", "votos": 0}

        response = self.criaEnquete()

        response = self.client.post(
            self.URL_ENQUETE+'1/respostas/',
            resposta, format='json')
        return response, resposta
