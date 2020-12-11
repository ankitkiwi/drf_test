"""Room Models"""
from django.db import models

# app imports
from item.models import Item
from utils.models import DateModel


class Room(DateModel, models.Model):
    """Model class for Room"""
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Item, related_name="room_item")
