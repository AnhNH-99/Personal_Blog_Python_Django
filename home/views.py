from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.contrib.sessions.models import Session
# Create your views here.


def index(request):
    user = None
    if request.session.get('user'):
        user = request.session['user']
    postnew = Post.objects.last()
    listPost = Post.objects.all()
    page = request.GET.get('page')
    if page is None:
        page = 1
    pageSize = 2 * page
    paginator = Paginator(listPost, pageSize)
    page_obj = paginator.get_page(1)
    Data = {'Post': page_obj, 'PostNew': postnew, 'User': user}
    return render(request, 'pages/home.html', Data)


class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = "pages/home.html"
    context_object_name = 'Post'
    paginate_by = 2


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            if request.session.get('user'):
                del request.session['user']
            request.session['user'] = user.username
            # Redirect to a success page.
            return HttpResponseRedirect("/")
        else:
            error = 'Account or password is incorrect'
            return render(request, 'pages/login.html', {'Error': error})
    return render(request, 'pages/login.html')

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return HttpResponseRedirect("/")