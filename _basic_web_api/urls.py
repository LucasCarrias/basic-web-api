from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('profile-posts/', include('profiles.profiles-posts.urls')),
]
