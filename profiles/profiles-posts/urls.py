from django.urls import path
from .views import ProfilePostsListView, ProfilePostsDetailView


urlpatterns = [
    path('', ProfilePostsListView.as_view(), name='profile-posts-list'),
    path('<int:pk>', ProfilePostsDetailView.as_view(), name='profile-posts-detail'),
]
