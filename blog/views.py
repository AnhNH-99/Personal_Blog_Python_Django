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
    post = get_object_or_404(Post, id = id)
    form = CommentForm()
    fromReply = ReplyForm()
    if request.method == 'POST':
        if request.POST.get("commentId", ""):
            commentId = request.POST.get("commentId", "")
            body = request.POST.get("body", "")
            comment = get_object_or_404(Comment, id = commentId)
            form = ReplyForm(request.POST, author=user, comment=comment)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)
        else:
            form = CommentForm(request.POST, author=user, post=post)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)
    return render(request, 'pages/post.html', {'post': post, 'form': form, 'fromReply': fromReply, 'User': username})


