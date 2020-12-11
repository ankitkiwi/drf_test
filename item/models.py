"""Item Models"""
from django.db import models

# app imports
from utils.models import DateModel


class Item(DateModel, models.Model):
    """Item Model"""
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        """String Representation of Item"""
        return str(self.name)
