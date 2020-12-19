from django.urls import path
from .views import api_url_list_view

urlpatterns = [
    path('', api_url_list_view),
]
