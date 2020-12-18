from rest_framework import serializers
from posts.models import Post


class PostCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail',
    )
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'comments']