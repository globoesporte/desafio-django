from rest_framework import serializers
from .models import Survey, Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        depth = 1
        fields = ['id', 'description', 'position', 'votes']


class SurveySerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Survey
        depth = 1
        fields = ['id', 'name', 'description', 'options']

    # http://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
    def create(self, validated_data):
        """
        Cria uma nova enquete
        :param validated_data:
        :return:
        """
        options_data = validated_data.pop('options', [])

        survey = Survey.objects.create(**validated_data)

        for option_data in options_data:
            Option.objects.create(survey=survey, **option_data)

        return survey

    def update(self, instance, validated_data):
        """
        Faz atualização em uma enquete ja existente
        :param instance:
        :param validated_data:
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
