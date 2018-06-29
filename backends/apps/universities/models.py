import uuid

from django.apps import apps as django_apps
from django.conf import settings
from django.db import models
from apps.users.models import User


class University(models.Model):
    name = models.CharField(max_length=40)
    addr_x = models.FloatField()
    addr_y = models.FloatField()


class Spot(models.Model):
    CATEGORY = (
        ('RS', 'Restaurant Single'),
        ('RD', 'Restaurant Duo'),
        ('RP', 'Restaurant Price'),
        ('CS', 'Cafe Single'),
        ('CD', 'Cafe Duo'),
        ('CP', 'Cafe Price'),
        ('PS', 'Pub Soju'),
        ('PD', 'Pub Duo'),
        ('PP', 'Pub Price'),
        ('HD', 'Hidden Day'),
        ('HN', 'Hidden Night')
    )
    university = models.ForeignKey(
        University,
        related_name='spots',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    addr_x = models.FloatField()
    addr_y = models.FloatField()
    picture = models.FileField(upload_to='pictures/')
    category = models.CharField(max_length=2, choices=CATEGORY)
    comment = models.CharField(max_length=100)
    is_validated = models.BooleanField(default=False)


class Story(models.Model):
    spot = models.ForeignKey(
        Spot,
        related_name='stories',
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=100, default=None)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
