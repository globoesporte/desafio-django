from rest_framework import serializers

from django.contrib.auth.models import User

from enqueteapp.models import Choice, Question

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'owner')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        depth = 1
        fields = ('id', 'choice_text', 'votes')

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'questions')
