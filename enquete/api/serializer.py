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


class EnqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquete
        # itens = ResourceRelatedField(queryset= Item.objects,  many=True)
        itens = serializers.HyperlinkedRelatedField(
            view_name='item-list',
            lookup_field='item',
            many=True,
            read_only=True)
        fields = ('id', 'uuid', 'nome', 'descricao', 'data_criacao', 'itens')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        enquete = EnqueteSerializer()
        fields = ('id', 'uuid', 'nome', 'descricao', 'data_criacao', 'valor', 'enquete')

    def create(self, validated_data):
        itemObj = validated_data
        item = Item.objects.create(**itemObj)

        return item
