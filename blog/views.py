from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Reply
from .forms import CommentForm, ReplyForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
# Create your views here.

def post(request, id):
    username = None
    user = None
    if request.session.get('user'):
        username = request.session['user']
        user = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, id=id)
    form = CommentForm()
    from_reply = ReplyForm()
    if request.method == 'POST':
        if request.POST.get("comment_id", ""):
            comment_id = request.POST.get("comment_id", "")
            body = request.POST.get("body", "")
            comment = get_object_or_404(Comment, id=comment_id)
            form = ReplyForm(request.POST, author=user, comment=comment)
            if form.is_valid():
                form.save()
                request.path += "?reply="+str(comment_id)
                return HttpResponseRedirect(request.path)
        else:
            form = CommentForm(request.POST, author=user, post=post)
            if form.is_valid():
                form.save()
                request.path += "?comment="+str(id)
                return HttpResponseRedirect(request.path)
    if request.GET.get('comment') is None and request.GET.get('reply') is None:
        view = get_object_or_404(Post, id=id).view + 1
        Post.objects.filter(id=id).update(view = view)
    post = get_object_or_404(Post, id=id)
    return render(request, 'pages/post.html', {'post': post, 'form': form, 'from_reply': from_reply, 'user': username})


def list_blog(request):
    user = None
    query = None
    if request.session.get('user'):
        user = request.session['user']
    list_post = Post.objects.all().order_by('-date')
    if request.GET.get('search'):
        query = request.GET.get('search')
        list_post = Post.objects.filter(title__icontains=query)
    page = request.GET.get('page')
    if page is None:
        page = 1
    page_size = 2
    paginator = Paginator(list_post, page_size)
    page_obj = paginator.get_page(page)
    data = {'posts': page_obj, 'user': user, 'search': query}
    return render(request, 'pages/blog.html', data)
