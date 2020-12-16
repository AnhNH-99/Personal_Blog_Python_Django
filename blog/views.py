from django.shortcuts import render
from blog.models import Post
# Create your views here.
def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/post.html', {'post': post})
