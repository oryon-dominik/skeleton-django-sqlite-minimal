""" base URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html')),
    path('', include('apps.users.urls', namespace="users")),
    path('admin/', admin.site.urls),
]
