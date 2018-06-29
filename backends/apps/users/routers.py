from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from apps.users.views import UserViewSet

user_router = SimpleRouter()

user_router.register(
    prefix=r'users',
    viewset=UserViewSet,
)