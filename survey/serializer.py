from rest_framework import serializers
from .models import Survey, Option

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        depth = 1
        fields = ['id', 'description', 'position', 'votes']


class SurveySerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        depth = 1
        fields = ['id', 'name', 'description', 'options']
