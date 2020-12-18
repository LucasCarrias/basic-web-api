from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Comment
from .serializers import CommentSerializer

class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer