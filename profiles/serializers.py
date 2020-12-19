from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("__all__")


class ProfileInfoSerializer(serializers.ModelSerializer):
    total_posts = serializers.IntegerField(read_only=True)
    total_comments = serializers.IntegerField(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'name', 'total_posts', 'total_comments']
