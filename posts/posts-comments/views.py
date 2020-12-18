from rest_framework.generics import ListAPIView, RetrieveAPIView
from posts.models import Post
from .serializers import PostCommentsSerializer


class PostCommentsListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerializer


class PostCommentsDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerializer