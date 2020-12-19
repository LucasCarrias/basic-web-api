from django.urls import path
from .views import PostListView, PostDetailView, PostDetailCommentListView, PostDetailCommentCRUDView


urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("<int:pk>/comments/", PostDetailCommentListView.as_view(), name="post-detail-comment-list"),
    path("<int:post_pk>/comments/<int:pk>", PostDetailCommentCRUDView.as_view(), name="post-detail-comment-detail"),
]
