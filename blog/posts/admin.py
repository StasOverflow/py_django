from django.contrib import admin

from django.contrib.auth.models import Permission
# Register your models here.
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    exclude = ('updated_on',)
    list_display = ('title', 'created_on',)
    list_filter = ('created_on', 'title', )


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('meta_keywords',)
    list_display = ('name', 'is_active', 'description', 'id')
    list_filter = ('description', 'name', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Permission)
