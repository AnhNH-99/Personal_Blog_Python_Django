from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from blog.models import Post
urlpatterns = [
   path('', views.index),
   path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path('register/', views.register, name="register"),
   path('<int:pk>/', views.post, name='post')
]