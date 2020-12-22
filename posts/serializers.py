from rest_framework import serializers
from .models import Post
from comments.models import Comment


class PostSerializer(serializers.ModelSerializer):
    userId = serializers.CharField(source="user_id")
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'userId']


class PostDetailCommentSerializer(serializers.ModelSerializer):
    postId = serializers.CharField(source="post_id")
    class Meta:
        model = Comment
        fields = ['name', 'body', 'email', "postId"]