from django.urls import path
from django.views.generic import TemplateView
from .views import api_url_list_view
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('', api_url_list_view),
    path('openapi', get_schema_view(
        title="Basic web API",
        description="APIzinha feita durante a disciplina de Programação para Internet",
        version="1.0.0"
    ), name='openapi-schema'),
    path('docs', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
