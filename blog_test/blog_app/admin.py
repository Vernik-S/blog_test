from django.contrib import admin

# Register your models here.
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_on')

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)