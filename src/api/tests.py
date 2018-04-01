from django.test import TestCase
from django.contrib.auth.models import User

from enqueteapp.models import Choice, Question
from .views import AllQuestionsView, QuestionView

from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate ,APIClient

from rest_framework import status

from json import dumps

class QuestionsAPITest(APITestCase):

    client = APIClient()

    def test_post_question(self):
        data = {
                'question_text': "lala",
        }
        
        all_questions_url = '/api'
        user = User.objects.create_superuser(username = "renatinho", email = "x@x.com" ,password = "x")
        self.client.force_authenticate(user = user)
        response = self.client.post(all_questions_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        question = Question.objects.get(id = 1)
        self.assertEqual(question.question_text, "lala")


    def test_put_question(self):
        data = {
                'question_text': "lala",
        }
        question = Question.objects.create(question_text="x")
        user = User.objects.create_superuser(username = "renatinho", password = "x",email = "x@x.com")
        self.client.force_authenticate(user = user)
        question_url = '/api/1'
        response = self.client.put(question_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        question = Question.objects.get(id = 1)
        self.assertEqual(question.question_text, "lala")

    def test_delete_question(self):
        question = Question.objects.create(question_text="x")
        user = User.objects.create_superuser(username = "renatinho", email = "x@x.com" ,password = "x")
        self.client.force_authenticate(user = user)
        question_url = '/api/1'
        response = self.client.delete(question_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ChoicesAPITest(APITestCase):

    client = APIClient()

    def test_choice_post(self):
        
        user = User.objects.create_superuser(username = "renatinho", email = "x@x.com" ,password = "x")
        question = Question.objects.create(question_text="x")
        data = {
                'question': 1, 
                'choice_text': "lala",
        }
        all_questions_url = '/api/choices'
        self.client.force_authenticate(user = user)
        response = self.client.post(all_questions_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        choice = Choice.objects.get(id = 1)
        self.assertEqual(choice.choice_text, "lala")

    def test_put_choice(self):
        data = {
                'question': 1,
                'choice_text': "y",
        }

        question = Question.objects.create(question_text="x")
        choice = Choice.objects.create(question = question, choice_text="x")
        user = User.objects.create_superuser(username = "renatinho", email = "x@x.com" ,password = "x")
        self.client.force_authenticate(user = user)
        choice_url= '/api/choices/1'
        response = self.client.put(choice_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        choice = Choice.objects.get(pk = 1)
        self.assertEqual(choice.choice_text, "y")


    def test_delete_choice(self):
        question = Question.objects.create(question_text="x")
        choice = Choice.objects.create(question = question , choice_text="x")
        user = User.objects.create_superuser(username = "renatinho", email = "x@x.com" ,password = "x")
        self.client.force_authenticate(user = user)
        choice_url = '/api/choices/1'
        response = self.client.delete(choice_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class VotesAPITest(APITestCase):

    client =  APIClient()
    
    def test_vote_post(self):
        question = Question.objects.create(question_text="x")
        choice = Choice.objects.create(question = question, choice_text="x")
        vote_url = '/api/choices/vote/1'
        response = self.client.post(vote_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        choice_after_post = Choice.objects.get(id=1)
        self.assertEqual(choice_after_post.votes, 1)
