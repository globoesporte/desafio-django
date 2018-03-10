from rest_framework import serializers

from polls import models


class OptionSerializer(serializers.ModelSerializer):
    number_of_votes = serializers.SerializerMethodField()

    class Meta:
        model = models.Option
        fields = '__all__'

    def get_number_of_votes(self, obj):
        return obj.votes_option.all().count()


class PollSerializer(serializers.ModelSerializer):
    options_poll = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Poll
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vote
        fields = '__all__'