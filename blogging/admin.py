from django.contrib import admin
from blogging.models import Post
from blogging.models import Category

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)