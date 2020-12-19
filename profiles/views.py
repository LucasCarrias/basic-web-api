from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Profile
from .serializers import ProfileSerializer, ProfileInfoSerializer
from rest_framework.response import Response

class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileInfoView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileInfoSerializer

    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()
        
        posts = profile.posts
        comments_count = sum([post.comments.count() for post in posts.all()])

        serializer = self.get_serializer(profile)
        
        data = serializer.data.copy()
        data.update({
            'total_posts':posts.count(),
            'total_comments': comments_count
        })
        
        return Response(data)
