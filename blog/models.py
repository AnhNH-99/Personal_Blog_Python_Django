from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(null = True)
    author = models.TextField(max_length = 255, null = True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

