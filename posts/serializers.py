from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    userId = serializers.CharField(source="user_id")
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'userId']