from django.contrib.auth.models import User

from rest_framework import status

from rest_framework.test import (
    force_authenticate,
    APIRequestFactory,
    APITestCase,
    APIClient,
)

from polls.models import (
    Poll,
    Option,
    Vote,
)


class PollsTest(APITestCase):
    client = APIClient()

    data_create = {
        'id': 1,
        'title': 'poll_title',
        'text': 'poll_text',
    }

    data_update = {
        'title': 'new_poll_title',
        'text': 'new_poll_text',
    }

    urls = {
        'create': '/api/polls/',
        'update': '/api/polls/1/',
        'delete': '/api/polls/1/',
    }

    def test_create_polls(self):
        # Creating temporary database objects
        user = User.objects.create(username='foo', password='bar', is_staff=True, is_superuser=True)

        # forcing auth on ai request
        self.client.force_authenticate(user=user)

        # create the request and get the response
        response = self.client.post(self.urls['create'], self.data_create, format='json')

        # asserts
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Poll.objects.count(), 1)
        self.assertEqual(Poll.objects.get().title, 'poll_title')
        self.assertEqual(Poll.objects.get().text, 'poll_text')

    def test_update_polls(self):
        # Creating temporary database objects
        user = User.objects.create(username='foo', password='bar', is_staff=True, is_superuser=True)
        poll = Poll.objects.create(title='poll_title', text='poll_text')

        # forcing auth on ai request
        self.client.force_authenticate(user=user)

        # create the request and get the response
        response = self.client.put(self.urls['update'], self.data_update, format='json')

        # asserts
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Poll.objects.get().title, 'new_poll_title')
        self.assertEqual(Poll.objects.get().text, 'new_poll_text')

    def test_delete_polls(self):
        # Creating temporary database objects
        user = User.objects.create(username='foo', password='bar', is_staff=True, is_superuser=True)
        poll = Poll.objects.create(title='poll_title', text='poll_text')

        # forcing auth on ai request
        self.client.force_authenticate(user=user)

        # create the request and get the response
        response = self.client.delete(self.urls['delete'], format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class OptionsTest(APITestCase):

    client = APIClient()

    data_create = {
        'id': 1,
        'text': 'option_text',
        'poll': 1,
    }

    data_update = {
        'id': 1,
        'text': 'option_text',
        'poll': 1,
    }

    urls = {
        'create': '/api/options/',
        'update': '/api/options/1/',
        'delete': '/api/options/1/',
    }

    def test_create_option(self):
        # Creating temporary database objects
        user = User.objects.create(username='foo', password='bar', is_staff=True, is_superuser=True)
        poll = Poll.objects.create(id=1, title='poll_title', text='poll_text')

        # forcing auth on ai request
        self.client.force_authenticate(user=user)

        # create the request and get the response
        response = self.client.post(self.urls['create'], self.data_create, format='json')
        
        # asserts
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Option.objects.count(), 1)
        self.assertEqual(Option.objects.get().text, 'option_text')
        self.assertEqual(Option.objects.get().poll, poll)

    def test_update_option(self):
        # Creating temporary database objects
        user = User.objects.create(username='foo', password='bar', is_staff=True, is_superuser=True)
        poll = Poll.objects.create(id=1, title='poll_title', text='poll_text')
        option = Option.objects.create(id=1, text='option_text', poll=poll)

        # forcing auth on ai request
        self.client.force_authenticate(user=user)

        # create the request and get the response
        response = self.client.put(self.urls['update'], self.data_update, format='json')

        # asserts
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Option.objects.get().text, 'option_text')
        self.assertEqual(Option.objects.get().poll, poll)

    def test_delete_option(self):
        # Creating temporary database objects
        user = User.objects.create(username='foo', password='bar', is_staff=True, is_superuser=True)
        poll = Poll.objects.create(id=1, title='poll_title', text='poll_text')
        option = Option.objects.create(id=1, text='option_text', poll=poll)

        # forcing auth on ai request
        self.client.force_authenticate(user=user)

        # create the request and get the response
        response = self.client.delete(self.urls['delete'], format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class VotesTest(APITestCase):

    client = APIClient()

    data_create = {
        'id': 1,
        'options': 1,
        'poll': 1,
    }

    data_update = {
        'id': 1,
        'options': 1,
        'poll': 1,
    }

    urls = {
        'create': '/api/vote/',
        'update': '/api/vote/1/',
        'delete': '/api/vote/1/',
    }

    def test_create_vote(self):
        # Creating temporary database objects
        poll = Poll.objects.create(id=1, title='poll_title', text='poll_text')
        option = Option.objects.create(id=1, text='option_text', poll=poll)

        # create the request and get the response
        response = self.client.post(self.urls['create'], self.data_create, format='json')

        # asserts
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.count(), 1)
        self.assertEqual(Vote.objects.get().poll, poll)
        self.assertEqual(Vote.objects.get().options, option)

    def test_update_vote(self):
        # Creating temporary database objects
        user = User.objects.create(username='foo', password='bar', is_staff=True, is_superuser=True)
        poll = Poll.objects.create(id=1, title='poll_title', text='poll_text')
        option = Option.objects.create(id=1, text='option_text', poll=poll)
        vote = Vote.objects.create(id=1, poll=poll, options=option)

        # forcing auth on ai request
        self.client.force_authenticate(user=user)

        # create the request and get the response
        response = self.client.put(self.urls['update'], self.data_update, format='json')

        # asserts
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vote.objects.get().poll, poll)
        self.assertEqual(Vote.objects.get().options, option)

    def test_delete_option(self):
        # Creating temporary database objects
        user = User.objects.create(username='foo', password='bar', is_staff=True, is_superuser=True)
        poll = Poll.objects.create(id=1, title='poll_title', text='poll_text')
        option = Option.objects.create(id=1, text='option_text', poll=poll)
        vote = Vote.objects.create(id=1, poll=poll, options=option)

        # forcing auth on ai request
        self.client.force_authenticate(user=user)

        # create the request and get the response
        response = self.client.delete(self.urls['delete'], format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
