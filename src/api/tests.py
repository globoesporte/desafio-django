from django.test import TestCase
from django.contrib.auth.models import User

from enqueteapp.models import Choice, Option
from .views import AllQuestionsView, QuestionView

from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate()

class AllQuestionsAPITest(APITestCase):

    def setUpTestData(cls):
        user1 = User.objects.create_user('test_user1', password ='xxx')
        user2 = User.objects.create_user('test_user2', password = 'yyy')

        question = Question.objects.create(
                question_text="texto", pub_date=datetime(2018,2,1))
        choice =  Choice.objects.create(question = question, choice_text = 'xxx')
        client = AllQuestionsView()

    def setUp(self):
        pass

    def test_get_questions(self):

        
    def test_post_question(self):
        pass

    def test_get_question_detail(self):
        pass
    
    def test_put_question(self):
        pass

    def test_delete_question(self):
        pass

    def test_get_votes(self):
        pass

    def test_post_vote(self):



