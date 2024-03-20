from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_on')

admin.site.register(Post, PostAdmin)
