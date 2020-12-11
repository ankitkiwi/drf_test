"""Utils Models"""
from django.db import models


class DateModel(models.Model):
    """Base model for create data and update date"""
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta Data"""
        abstract = True
