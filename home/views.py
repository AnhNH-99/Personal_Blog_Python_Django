from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from blog.models import Post
from .models import About
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    user = None
    if request.session.get('user'):
        user = request.session['user']
    about = About.objects.last()
    list_post = Post.objects.all().order_by('-date')
    page = request.GET.get('page')
    if page is None:
        page = 1
    page_size = 2 * int(page)
    paginator = Paginator(list_post, page_size)
    page_obj = paginator.get_page(1)
    if int(page) > 1:
        page_obj.next_page_number = int(page) + 1
    data = {'posts': page_obj, 'about': about, 'user': user}
    return render(request, 'pages/home.html', data)

def about(request):
    user = None
    if request.session.get('user'):
        user = request.session['user']
    about = About.objects.last()
    data = {'about': about, 'user': user}
    return render(request, 'pages/about.html', data)

def register(request):
    user = None
    if request.session.get('user'):
        user = request.session['user']
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Sign Up Success"
            return HttpResponseRedirect('/', {'message': message, 'user': user})
    return render(request, 'pages/register.html', {'form': form, 'user': user})

def login(request):
    user = None
    if request.session.get('user'):
        user = request.session['user']
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
            message = "Sign In Success"
            return HttpResponseRedirect("/", {'message': message, 'user': user})
        else:
            error = 'Account or password is incorrect'
            return render(request, 'pages/login.html', {'error': error, 'user': user})
    return render(request, 'pages/login.html', {'user': user})

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return HttpResponseRedirect("/")