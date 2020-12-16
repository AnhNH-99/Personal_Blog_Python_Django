from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
from blog.models import Post
# Create your views here.
def index(request):
    Data = {'Post': Post.objects.all(), 'PostNew': Post.objects.last()}
    return render(request, 'pages/home.html', Data)

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post.html', {'post': post})


