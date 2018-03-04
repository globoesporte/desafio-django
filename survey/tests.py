from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Survey, Option
from .serializer import SurveySerializer


class GetSurveyTest(APITestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminadmin')
        self.client.login(username='admin', password='adminadmin')
        self.survey = Survey.objects.create(name="teste", description="teste")

    def test_can_get_surveys(self):
        """
        Checa se consegue pegar a lista de todas as enquetes
        """
        url = reverse('survey-general')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_survey(self):
        """
        Checa se consegue pegar as informações de uma unica enquete
        """
        url = reverse('survey-specific', args=[self.survey.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SaveSurveyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminadmin')
        self.client.login(username='admin', password='adminadmin')
        self.data = {'name': 'Name', 'description': 'Description'}

    def test_can_create_survey(self):
        """
        Teste de criação de enquete
        """
        url = reverse('survey-general')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateSurveyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminadmin')
        self.client.login(username='admin', password='adminadmin')
        self.survey = Survey.objects.create(name="Name", description="Description")
        self.data = SurveySerializer(self.survey).data
        self.data.update({'name': 'Other Name', 'description': 'Other Description'})

    def test_can_update_survey(self):
        """
        Teste de atualização da enquete
        """
        url = reverse('survey-specific', args=[self.survey.id])
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data.get('name'), Survey.objects.get(pk=self.survey.id).name)
        self.assertEqual(self.data.get('description'), Survey.objects.get(pk=self.survey.id).description)


class DeleteSurveyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminadmin')
        self.client.login(username='admin', password='adminadmin')
        self.survey = Survey.objects.create(name="Name", description="Description")

    def test_can_delete_survey(self):
        """
        Teste de deletar enquete
        """
        url = reverse('survey-specific', args=[self.survey.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        try:
            survey = Survey.objects.get(pk=self.survey.id)
            raise AssertionError("O objeto ainda existe!!")
        except ObjectDoesNotExist:
            pass # Não precisa fazer nada, o objeto realmente não existe


class VoteTest(APITestCase):
    def setUp(self):
        self.survey = Survey.objects.create(name="Name", description="Description")
        self.option = Option.objects.create(description="Description", position=1, survey=self.survey)
        self.data = {'id': self.option.id}

    def test_can_vote(self):
        """
        teste de voto
        """
        url = reverse('vote')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Option.objects.get(pk=self.option.id).votes, 1)

