"""Room View"""
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from utils.serializers import RoomSerializer, RoomListSerializer
from room.models import Room


class RoomViewSet(viewsets.ModelViewSet):
    """Room ViewSet"""
    queryset = Room.objects.all().order_by('id')
    serializer_class = RoomSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        get serializer class
        :return:
        """
        serializer_class = RoomSerializer

        if self.request.method == 'GET':
            serializer_class = RoomListSerializer

        return serializer_class
