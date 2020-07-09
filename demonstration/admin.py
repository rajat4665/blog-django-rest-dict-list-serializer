from django.contrib import admin
from .models import (
    Blog, BlogPost, User, Comment
)

admin.site.register(Blog)
admin.site.register(BlogPost)
admin.site.register(User)
admin.site.register(Comment)
