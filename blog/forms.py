from django import forms
from django.forms import fields
from .models import Comment, Reply
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()
    class Meta:
        model = Comment
        fields = ["body"]

class ReplyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.comment = kwargs.pop('comment', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        reply = super().save(commit=False)
        reply.author = self.author
        reply.comment = self.comment
        reply.save()
    class Meta:
        model = Reply
        fields = ["body"]