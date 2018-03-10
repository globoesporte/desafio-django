from rest_framework import serializers
from .models import Survey, Options


class OptionViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        depth = 1
        fields = ['id', 'option', 'votes']


class SurveySerializer(serializers.ModelSerializer):
    options = OptionViewSerializer(many=True)

    class Meta:
        model = Survey
        fields = ('id', 'description', 'options', 'active')

    def create(self, validated_data):
        options_data = validated_data.pop('options', [])
        survey = Survey.objects.create(**validated_data)

        for option_data in options_data:
            Options.objects.create(survey=survey, **option_data)

        return survey

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.active = validated_data.get('active',
                                             instance.active)
        instance.save()
        return instance


class OptionsSerializer(serializers.ModelSerializer):
    survey = serializers.PrimaryKeyRelatedField(queryset=Survey.objects.all())

    class Meta:
        model = Options
        fields = ('id', 'option', 'votes', 'survey')

    def create(self, validated_data):
        option = Options.objects.create(**validated_data)
        return option

    def update(self, instance, validated_data):
        instance.position = validated_data.get('survey', instance.survey)
        instance.option = validated_data.get('option', instance.option)
        instance.votes = validated_data.get('votes', instance.votes)
        instance.save()
        return instance
