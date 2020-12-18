from rest_framework.generics import ListAPIView, RetrieveAPIView
from profiles.models import Profile
from .serializers import ProfilePostSerializer


class ProfilePostsListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer


class ProfilePostsDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer