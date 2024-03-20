from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

from blog_app.models import Post, Comment
from blog_app.forms import PostForm, CommentForm, LoginForm




def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog_app/index.html", context)

def new_post(request):
    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect('/login/')


def new_comment(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                post_id=form.cleaned_data["post_id"],
                text=form.cleaned_data["text"],
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    context = {
        "form": CommentForm(),
    }

    return render(request, "blog_app/new_comment.html", context)


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password =  form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'LoggedIn successfully')
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request, 'blog_app/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/')