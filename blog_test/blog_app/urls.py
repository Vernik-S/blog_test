from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("new_post/", views.new_post, name="new_post"),
    path("new_comment/", views.new_comment, name="new_comment"),
    path("login/", views.user_login, name="login"),
]