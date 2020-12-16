from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    postnew = Post.objects.last()
    listPost = Post.objects.all()
    
    page = request.GET.get('page')
    if page is None:
        page = 1
    pageSize = 2 * page
    paginator = Paginator(listPost, pageSize)
    # pageNumber = request.GET.get('page')
    # page_obj = paginator.get_page(pageNumber)
    # try:
    #     page_obj = paginator.page(pageNumber)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(1)
    Data = {'Post': page_obj, 'PostNew': postnew}
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
