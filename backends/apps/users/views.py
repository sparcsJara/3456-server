from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from apps.users.models import User
from apps.users.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
