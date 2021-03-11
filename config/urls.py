""" base URL Configuration

"""
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), {"TITLE": settings.PROJECT_TITLE}),
    path('', include('apps.users.urls', namespace="users")),
]

if settings.DEBUG:
    # debug toolbar
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]
