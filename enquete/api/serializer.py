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
    class Meta:
        model = Item
        enquete = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        fields = ('id', 'uuid', 'nome', 'descricao', 'data_criacao', 'valor', 'enquete')

    def create(self, validated_data):
        itemObj = validated_data
        item = Item.objects.create(**itemObj)

        return item

class EnqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquete
        itens = ItemSerializer(many=True, read_only=True)
        fields = ('id', 'uuid', 'nome', 'descricao', 'data_criacao', 'itens')

class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        enquete = EnqueteSerializer()
        item = ItemSerializer()
        fields = ('id', 'uuid', 'data_criacao', 'item', 'enquete')

    def create(self, validated_data):
        itemObj = validated_data
        item = Voto.objects.create(**itemObj)

        return item
