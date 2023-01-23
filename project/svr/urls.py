from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from svr.views import ClientViewSet, OrderViewSet, PositionViewSet, TempViewSet, \
    ping, get_history

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'position', PositionViewSet)
router.register(r'order', OrderViewSet)
router.register(r'temp', TempViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('ping/', ping),
    path('get_history/', get_history),
    path('get_history/<int:pk>', get_history),
]
