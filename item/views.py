"""Item View"""
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from utils.serializers import ItemSerializer
from item.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    """Item ViewSet"""
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
