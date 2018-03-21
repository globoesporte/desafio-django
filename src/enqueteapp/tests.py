from django.test import TestCase
from .models import Choice, Question
from datetime import datetime

class QuestionTest(TestCase):

    def setUpTestData(cls):
        question = Question.objects.create(
                question_text="texto", pub_date=datetime(2018,2,1))

    def test_question_text(self):
        question = Question.objects.get(id=1)
        return self.assertEqual(question.question_text, 'texto')

    def test_pub_date(self):
        question = Question.objects.get(id=1)
        return self.assertEqual(datetime(2018,2,1), question.pub_date)

    def test_question_txt_max_len(self):
        question = Question.objects.get(id=1)
        max_len = question._meta.get_field('question_text').max_length
        return self.assertEqual(max_len,200)


class ChoiceTest(TestCase):

    def setUpTestData(cls):
        question = Question.objects.create(
                question_text="texto", pub_date=datetime(2018,2,1))
        choice =  Choice.objects.create(question = question, choice_text = 'xxx')

    def test_question(self):
        choice = Choice.object.get(id=1)
        return self.assertEqual(choice.question.id, 1) 

    def test_choice_text(self):
        choice = Choice.object.get(id=1)
        return self.assertEqual(choice.choice_text, 'xxx')

    def test_vote(self):
        choice = Choice.objects.get(id=1) 
        choice.add_vote()
        return self.assertEqual(1, choice.votes)
