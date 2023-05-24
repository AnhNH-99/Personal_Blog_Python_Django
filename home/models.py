from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(null = True)
    author = models.TextField(max_length = 255, null = True)
