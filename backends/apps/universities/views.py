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

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Spot.objects.all(is_validated=True)
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(spot__category=category)
        return queryset

class StoryViewset(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
