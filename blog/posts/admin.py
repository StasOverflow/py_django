from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    exclude = ('updated_on',)
    list_display = ('title', 'created_on',)
    list_filter = ('created_on', 'title', )


admin.site.register(Post, PostAdmin)
