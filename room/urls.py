"""Room Url Patterns"""
from rest_framework import routers
from room import views

router = routers.SimpleRouter()
router.register('room', views.RoomViewSet)


urlpatterns = router.urls
