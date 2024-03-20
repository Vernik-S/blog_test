from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from blog_app.models import Post
from blog_app.forms import PostForm

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog_app/index.html", context)

def new_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                title=form.cleaned_data["title"],
                text=form.cleaned_data["text"],
            )
            post.save()
            return HttpResponseRedirect(request.path_info)

    context = {
        "form": PostForm(),
    }

    return render(request, "blog_app/new_post.html", context)
