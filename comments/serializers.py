from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    postId = serializers.CharField(source="post_id")
    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'body', 'postId']