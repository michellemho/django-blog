from django.contrib import admin
from blogging.models import Post
from blogging.models import Category

# Register your models here.

# admin.site.register(Post)
# admin.site.register(Category)

class CategorizationInline(admin.TabularInline):
    model = Category.posts.through
    extra = 0
    max_num = 4
    min_num = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategorizationInline,
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # inlines = [
    #     CategorizationInline,
    # ]
    exclude = ['posts']