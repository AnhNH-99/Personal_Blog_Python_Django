from django.contrib import admin
from .models import About

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

admin.site.register(About, AboutAdmin)

