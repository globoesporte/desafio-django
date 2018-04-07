from rest_framework import serializers

from enqueteapp.models import Choice, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:

        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')
