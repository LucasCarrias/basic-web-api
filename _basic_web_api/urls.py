from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('profile-posts/', include('profiles.profiles-posts.urls')),
    path('posts-comments/', include('posts.posts-comments.urls')),
    path('api-root/', include('api_root.urls')),
]
