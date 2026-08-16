from django.urls import path

from . import views
from .views import projects

urlpatterns = [
    path('', projects, name='projects'),
    path(
        '<slug:slug>/',
        views.project_detail,
        name='project_detail'
    ),
]
