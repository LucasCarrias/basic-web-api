from django.urls import path
from .views import ProfileListView, ProfileDetailView, ProfileInfoView

urlpatterns = [
    path('', ProfileListView().as_view(), name="profile-list"),
    path('<int:pk>', ProfileDetailView().as_view(), name="profile-detail"),
    path('<int:pk>/info', ProfileInfoView().as_view(), name="profile-info"),
]
