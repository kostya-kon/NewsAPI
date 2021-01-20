from django.contrib import admin

from .models import Post, Comment

# register models for easy creating by admin panel
admin.site.register(Post)
admin.site.register(Comment)
