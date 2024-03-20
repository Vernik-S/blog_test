from django.shortcuts import render

# Create your views here.

from blog_app.models import Post

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog_app/index.html", context)