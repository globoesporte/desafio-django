from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from rest_framework.test import APIClient

from requests.auth import HTTPBasicAuth

from .test_util import *
from .test_base import *


# Teste onde DEVE acontecer e o usuário autenticado
class RespostassRESTAutenticadoDeveTests(BaseRESTDeveTests):

    def setUp(self):
        super().setUp()
        self.client.login(username='testuser', password='testing')

    def test_deve_criar_resposta_via_post_autenticado(self):
        response, resposta = self.criaResposta()

        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data, resposta)

    def test_deve_retornar_lista_resposta_da_enquete_autenticado(self):
        response, resposta = self.criaResposta()

        response = self.client.get(
            self.URL_ENQUETE + '1/respostas/',
            None, format='json')

        self.assertEquals(response.status_code, 200)

        listaRespostas = self.bodyRetorno.pop('respostas')
        listaRespostas.append(resposta)

        self.assertEquals(response.status_code, 200)
        self.assertTrue(equalListDicts(response.data, listaRespostas))

    def test_deve_retornar_resposta_pelo_id_autenticado(self):
        response, resposta = self.criaResposta()

        response = self.client.get(
            self.URL_RESPOSTA + '4/',
            None, format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, resposta)

    def test_deve_alterar_resposta_pelo_id_autenticado(self):
        response, resposta = self.criaResposta()

        update = {"opcao": "Andorinhas brasileiras", "votos": 2}

        response = self.client.put(
            self.URL_RESPOSTA + '1/',
            update, format='json')

        update['id'] = 1

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, update)

    def test_deve_excluir_resposta_pelo_id_autenticado(self):
        response, resposta = self.criaResposta()

        response = self.client.delete(
            self.URL_RESPOSTA + '1/',
            None, format='json')

        self.assertEquals(response.status_code, 204)

    def teste_deve_adicionar_voto_autenticado(self):
        response, resposta = self.criaResposta()

        response = self.client.post(
            self.URL_RESPOSTA + '1/voto/',
            None, format='json')

        self.assertEquals(response.status_code, 201)


# Teste onde DEVE acontecer a senteça que dá nome ao método.
# Não autenticado
class RespostasRESTNAODeveTests(BaseRESTDeveTests):

    def setUp(self):
        super().setUp()

    def test_deve_criar_resposta_via_post_NAO_autenticado(self):
        response, resposta = self.criaResposta()

        self.assertEquals(response.status_code, 401)

    def test_deve_retornar_lista_resposta_da_enquete_NAO_autenticado(self):
        response, resposta = self.criaResposta()

        response = self.client.get(
            self.URL_ENQUETE + '1/respostas/',
            None, format='json')

        self.assertEquals(response.status_code, 401)

    def test_deve_retornar_resposta_pelo_id_NAO_autenticado(self):
        response, resposta = self.criaResposta()

        response = self.client.get(
            self.URL_RESPOSTA + '4/',
            None, format='json')

        self.assertEquals(response.status_code, 401)

    def test_deve_alterar_resposta_pelo_id_NAO_autenticado(self):
        response, resposta = self.criaResposta()

        update = {"opcao": "Andorinhas brasileiras", "votos": 2}

        response = self.client.put(
            self.URL_RESPOSTA + '1/',
            update, format='json')

        update['id'] = 1

        self.assertEquals(response.status_code, 401)

    def test_deve_excluir_resposta_pelo_id_NAO_autenticado(self):
        response, resposta = self.criaResposta()

        response = self.client.delete(
            self.URL_RESPOSTA + '1/',
            None, format='json')

        self.assertEquals(response.status_code, 401)

    def teste_DEVE_adicionar_voto_NAO_autenticado(self):
        self.client.login(username='testuser', password='testing')
        response, resposta = self.criaResposta()

        self.client.logout()

        response = self.client.post(
            self.URL_RESPOSTA + '1/voto/',
            None, format='json')

        self.assertEquals(response.status_code, 201)
        self.assertTrue(equalDicts(response.data, {"votos": 1}))
