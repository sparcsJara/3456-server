from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from apps.universities.models import *
from apps.universities.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

# Create your views here.

class UniversityViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.filter(is_validated=True)
    serializer_class = SpotSerializer

class StoryViewset(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
