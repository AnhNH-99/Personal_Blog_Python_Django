from django.contrib import admin
from .models import Post, Comment, Reply
# Register your models here.

class ReplyInline(admin.StackedInline):
    model = Reply

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'date']
    list_filter = ['date']
    search_fields = ['author']
    inlines = [ReplyInline]
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
