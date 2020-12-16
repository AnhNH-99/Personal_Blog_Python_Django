from django.conf.urls import url
from django.urls import path
from . import views
from .models import Post
urlpatterns = [
    path('<int:pk>/', views.post, name='post')
]
