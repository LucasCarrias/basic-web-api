from rest_framework import serializers
from profiles.models import Profile


class ProfilePostSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='post-detail',
    )
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'posts']