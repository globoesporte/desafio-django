from rest_framework import serializers
from  .models import Survey, Options 


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'description','activate')
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=False, allow_blank=True, max_length=100)
    activate = BooleanField(default=False)
    def create(self, validated_data):
        return Survey.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.save()
        return instance
