"""Serializer Class"""
from rest_framework import serializers

from room.models import Room
from item.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """Item Serializer"""
    class Meta:
        """Meta Class"""
        model = Item
        fields = ('id', 'name', 'price')


class RoomSerializer(serializers.ModelSerializer):
    """Room Serializer"""
    class Meta:
        """Meta Class"""
        model = Room
        fields = '__all__'


class RoomListSerializer(serializers.ModelSerializer):
    """Room List Serializer"""
    items = ItemSerializer(many=True)

    class Meta:
        """Meta Class"""
        model = Room
        fields = ('id', 'name', 'items')
