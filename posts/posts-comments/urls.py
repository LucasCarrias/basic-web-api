from django.urls import path
from .views import PostCommentsListView, PostCommentsDetailView


urlpatterns = [
    path('', PostCommentsListView.as_view(), name='post-comments-list'),
    path('<int:pk>', PostCommentsDetailView.as_view(), name='post-comments-detail'),
]
