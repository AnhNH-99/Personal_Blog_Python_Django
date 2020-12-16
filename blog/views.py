from django.shortcuts import render
from blog.models import Post
# Create your views here.
def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'pages/post.html', {'post': post})
