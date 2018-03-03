from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, RequestsClient
from django.contrib.auth.models import User


class GetSurveyTest(APITestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminadmin')
        self.client.login(username='admin', password='adminadmin')

    def test_can_get_surveys(self):
        url = reverse('survey-general')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)