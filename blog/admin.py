from django.contrib import admin
from .models import Post, Category, Task

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Task)