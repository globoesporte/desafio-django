from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from rest_framework.test import APIClient

from requests.auth import HTTPBasicAuth

from .test_util import *
from .test_base import *


# Teste onde DEVE acontecer a senteça que dá nome ao método
# e usuário autenticado
class EnquetesRESTAutenticadoDeveTests(BaseRESTDeveTests):

    def setUp(self):
        super().setUp()
        self.client.login(username='testuser', password='testing')
        self.response = self.criaEnquete()

    def test_deve_criar_enquete_via_post_autenticado(self):

        self.assertEquals(self.response.status_code, 201)
        self.assertTrue(equalDicts(self.response.data, self.bodyRetorno))

    def test_deve_retornar_lista_enquete_autenticado(self):
        response = self.client.get(
            self.URL_ENQUETE,
            None, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(equalDicts(response.data[0], self.bodyRetorno))

    def test_deve_retornar_enquete_pelo_id_autenticado(self):
        response = self.client.get(
            self.URL_ENQUETE+'1/',
            None, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(equalDicts(response.data, self.bodyRetorno))

    def test_deve_alterar_enquete_pelo_id_autenticado(self):
        newbody = self.body.copy()
        newbody.pop("respostas")
        newbody["ativa"] = False

        response = self.client.put(
            self.URL_ENQUETE+'1/',
            newbody, format='json')
        self.assertEquals(response.status_code, 200)

    def test_deve_excluir_enquete_pelo_id_autenticado(self):
        responde = self.criaEnquete()

        response = self.client.delete(
            self.URL_ENQUETE+'1/',
            None, format='json')
        self.assertEquals(response.status_code, 204)

# Teste onde NÃO DEVE acontecer a senteça que dá nome ao método e
# Não autenticado


class EnquetesRESTNAODeveNaoAutenticadoTests(BaseRESTDeveTests):
    def setUp(self):
        super().setUp()
        self.response = self.criaEnquete()

    def test_NAO_deve_criar_enquete_via_post_NAO_autenticado(self):

        response = self.criaEnquete()

        self.assertEquals(response.status_code, 401)

    def test_NAO_deve_retornar_lista_enquete_NAO_autenticado(self):
        response = self.client.get(
            self.URL_ENQUETE,
            None, format='json')
        self.assertEquals(response.status_code, 401)

    def test_NAO_deve_retornar_enquete_pelo_id_NAO_autenticado(self):
        response = self.client.get(
            self.URL_ENQUETE+'1/',
            None, format='json')
        self.assertEquals(response.status_code, 401)

    def test_NAO_deve_alterar_enquete_pelo_id_NAO_autenticado(self):
        newbody = self.body.copy()
        newbody.pop("respostas")
        newbody["ativa"] = False

        response = self.client.put(
            self.URL_ENQUETE+'1/',
            newbody, format='json')
        self.assertEquals(response.status_code, 401)

    def test_NAO_deve_excluir_enquete_pelo_id_NAO_autenticado(self):
        responde = self.criaEnquete()

        response = self.client.delete(
            self.URL_ENQUETE+'1/',
            None, format='json')
        self.assertEquals(response.status_code, 401)
