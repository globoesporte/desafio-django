import sys
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import (
    APIRequestFactory,
    APIClient,
    APITestCase,
    force_authenticate,
)

from core.models import Options,Survey


class TestSurvey(APITestCase):
    client = APIClient()

    createsurvey = {
        'description': 'test_title',
        'active': True,
    }

    updatesurvey = {
        'description': 'test_title_update',
        'active': False,
    }

    urls = {
        'create': '/api/surveys/',
        'update': '/api/surveys/1',
        'delete': '/api/surveys/1',
    }

    def test_createsurveys(self):
        user = User.objects.create(username='testadm', password='testadm', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=user)
        response = self.client.post(self.urls['create'], self.createsurvey)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(Survey.objects.get().description, 'test_title')
        self.assertEqual(Survey.objects.get().active, True)

    def test_updatesurveys(self):
        user = User.objects.create(username='testadm', password='testadm', is_staff=True, is_superuser=True)
        survey = Survey.objects.create(description='test_title', active=True)
        self.client.force_authenticate(user=user)
        response = self.client.put(self.urls['update'], self.updatesurvey)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Survey.objects.get().description, 'test_title_update')
        self.assertEqual(Survey.objects.get().active, False)

    def test_deletesurveys(self):
        user = User.objects.create(username='testadm', password='testadm', is_staff=True, is_superuser=True)
        survey = Survey.objects.create(description='test_title', active=True)
        self.client.force_authenticate(user=user)
        response = self.client.delete(self.urls['delete'])
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class TestOption(APITestCase):
    client = APIClient()

    createoption = {
        'option': 'test_option',
        'survey': 1,
    }

    updateoption = {
        'option': 'test_option_update',
    }

    urls = {
        'create': '/api/options/',
        'update': '/api/options/survey=1/option=1',
        'delete': '/api/options/survey=1/option=1',
    }

    def test_createoptions(self):
        user = User.objects.create(username='testadm', password='testadm', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=user)
        Survey.objects.create(description='test_title', active=True)
        response = self.client.post(self.urls['create'], self.createoption)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Options.objects.count(), 1)
        self.assertEqual(Options.objects.get().option, 'test_option')
        self.assertEqual(Options.objects.get().survey,Survey.objects.get())
        self.assertEqual(Options.objects.get().votes, 0)

    def test_updateoptions(self):
        user = User.objects.create(username='testadm', password='testadm', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=user)
        Survey.objects.create(description='test_title', active=True)
        response = self.client.post(self.urls['create'], self.createoption)
        response = self.client.put(self.urls['update'], self.updateoption)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Options.objects.count(), 1)
        self.assertEqual(Options.objects.get().option, 'test_option_update')
        self.assertEqual(Options.objects.get().survey,Survey.objects.get())
        self.assertEqual(Options.objects.get().votes, 0)


    def test_deleteoptions(self):
        user = User.objects.create(username='testadm', password='testadm', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=user)
        Survey.objects.create(description='test_title', active=True)
        response = self.client.post(self.urls['create'], self.createoption)
        response = self.client.delete(self.urls['delete'])
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class TestVote(APITestCase):
    client = APIClient()
    createoption = {
        'option': 'test_option',
        'survey': 1,
    }
    createoption2 = {
        'option': 'test_option2',
        'survey': 1,
    }

    urloption = '/api/options/'
       
    urls = {
        'create': '/api/vote/survey=1/option=1',
        'update': '/api/vote/survey=1/old_option=1/new_option=2',
        'delete': '/api/vote/survey=1/option=1',
    }

    def test_createvote(self):
        user = User.objects.create(username='testadm', password='testadm', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=user)
        Survey.objects.create(description='test_title', active=True)
        response = self.client.post(self.urloption, self.createoption)
        response = self.client.post(self.urls['create'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Options.objects.count(), 1)
        self.assertEqual(Options.objects.get().votes, 1)
    
    def test_updatevote(self):
        user = User.objects.create(username='testadm', password='testadm', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=user)
        Survey.objects.create(description='test_title', active=True)
        response = self.client.post(self.urloption, self.createoption)
        response = self.client.post(self.urloption, self.createoption2)
        response = self.client.post(self.urls['create'])
        self.assertEqual(Options.objects.count(), 2)
        self.assertEqual(Options.objects.get(pk=1).votes, 1)
        self.assertEqual(Options.objects.get(pk=2).votes, 0)
        response = self.client.put(self.urls['update'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Options.objects.get(pk=1).votes, 0)
        self.assertEqual(Options.objects.get(pk=2).votes, 1)

    def test_deletevote(self):
        user = User.objects.create(username='testadm', password='testadm', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=user)
        Survey.objects.create(description='test_title', active=True)
        response = self.client.post(self.urloption, self.createoption)
        response = self.client.post(self.urls['create'])
        response = self.client.delete(self.urls['delete'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Options.objects.get().votes, 0)

