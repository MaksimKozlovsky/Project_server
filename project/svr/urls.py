from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from svr.views import ClientViewSet, OrderViewSet, CommentViewSet, DeliveryViewSet, CatalogViewSet, ExtraViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'catalog', CatalogViewSet)
router.register(r'order', OrderViewSet)
router.register(r'extra', ExtraViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'delivery', DeliveryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
