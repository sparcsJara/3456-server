from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.universities.views import UniversityViewSet, SpotViewSet, StoryViewset

router = SimpleRouter()

router.register(
    prefix=r'universities',
    viewset=UniversityViewSet,
)

router.register(
    prefix=r'spots',
    viewset=SpotViewSet,
)

router.register(
    prefix=r'stories',
    viewset=StoryViewset,
)

