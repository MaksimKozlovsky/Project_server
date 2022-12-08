from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'all_users', )
router.register(r'all_company', )


urlpatterns = [
    path('', include(router.urls)),
]
