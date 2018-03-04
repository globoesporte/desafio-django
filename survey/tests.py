from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Survey, Option


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
        url = reverse('survey-general')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
