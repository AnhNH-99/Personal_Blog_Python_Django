from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from blog.models import Post
from django.conf.urls import url
urlpatterns = [
   url(r'^$', views.index),
   path('login/', views.login, name="login"),
   path('logout/',views.logout,name='logout'),
   path('register/', views.register, name="register")
]