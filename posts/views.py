from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from comments.models import Comment
from .serializers import PostSerializer, PostDetailCommentSerializer
from rest_framework.response import Response
from rest_framework import status

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailCommentListView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = PostDetailCommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return super().get_queryset().filter(post_id=post_id)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['postId'] = self.kwargs.get('pk')
        

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PostDetailCommentCRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = PostDetailCommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        return super().get_queryset().filter(post_id=post_id)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        data = request.data.copy()
        data['postId'] = self.kwargs.get('post_pk')
        
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    
