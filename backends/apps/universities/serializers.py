from apps.universities.models import *
from rest_framework import serializers
from django.conf import settings

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story,
        fields = '__all__'
        read_only_fields = (
            'created_time',
            'updated_time',
        )


class SpotSerializer(serializers.ModelSerializer):
    stories = StorySerializer(many=True, read_only=True)
    class Meta:
        model = Spot,
        fields = (
            'id',
            'university',
            'title',
            'addr_x',
            'addr_y',
            'picture',
            'category',
            'comment',
            'stories'
        )


class UniversitySerializer(serializers.ModelSerializer):
    spots = SpotSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = (
            'name',
            'addr_x',
            'addr_y',
            'spots'
        )
        # auto_now_add나 auto_now가 true이면 read_only_fields여야 함.
