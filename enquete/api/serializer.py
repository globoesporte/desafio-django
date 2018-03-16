from django.contrib.auth.models import User, Group
from api.models import Enquete, Item, Voto
from rest_framework import serializers
from rest_framework_json_api.relations import ResourceRelatedField
import sys
import logging

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ItemSerializer(serializers.ModelSerializer):
    enquete = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Item
        fields = ('id', 'uuid', 'nome', 'descricao', 'data_criacao', 'valor', 'enquete')

    def create(self, validated_data):
        itemObj = validated_data
        item = Item.objects.create(**itemObj)

        return item

class EnqueteSerializer(serializers.ModelSerializer):
    itens = ItemSerializer(many=True)
    class Meta:
        model = Enquete
        fields = ('id', 'uuid', 'nome', 'descricao', 'data_criacao', 'itens')

class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        fields = ('id', 'uuid', 'data_criacao', 'item')

    # def create(self, validated_data):
    #     return Voto.objects.create(**validated_data)
