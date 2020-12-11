"""Item Url Patterns"""
from rest_framework import routers
from item import views

router = routers.SimpleRouter()
router.register('item', views.ItemViewSet)


urlpatterns = router.urls
