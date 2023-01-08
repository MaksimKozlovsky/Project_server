from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from svr.views import ClientViewSet, OrderViewSet, PositionViewSet, ExtraViewSet, \
    ping

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'position', PositionViewSet)
router.register(r'order', OrderViewSet)
router.register(r'extra', ExtraViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('ping/', ping),
]
