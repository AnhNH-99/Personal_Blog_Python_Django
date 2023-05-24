from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
   path('', views.list_blog, name="blog"),
   path('<int:id>/', views.post, name='post'),
]