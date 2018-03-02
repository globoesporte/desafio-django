from rest_framework import serializers
from .models import Survey, Option


class OptionSerializer(serializers.ModelSerializer):
    survey = serializers.PrimaryKeyRelatedField(queryset=Survey.objects.all())

    class Meta:
        model = Option
        depth = 1
        fields = ['id', 'description', 'position', 'votes', 'survey']

    def update(self, instance, validated_data):
        """
        Faz atualização em uma opção ja existente
        :param instance:
        :param validated_data:
        """
        instance.position = validated_data.get('position', instance.position)
        instance.description = validated_data.get('description', instance.description)
        instance.votes = validated_data.get('votes', instance.votes)
        instance.save()
        return instance

    def create(self, validated_data):
        """
        Cria uma nova opção
        :param validated_data:
        :return:
        """
        print(validated_data)
        option = Option.objects.create(**validated_data)

        return option


# Serializer usado somente para mostrar as opções de enquete.
class OptionViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        depth = 1
        fields = ['id', 'description', 'position', 'votes']


class SurveySerializer(serializers.ModelSerializer):
    options = OptionViewSerializer(many=True)

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
