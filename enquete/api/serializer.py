from django.contrib.auth.models import User, Group
from api.models import Enquete, Item, Voto
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class EnqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquete
        fields = ('id', 'uuid', 'nome', 'descricao', 'data_criacao')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'uuid', 'nome', 'descricao', 'data_criacao')