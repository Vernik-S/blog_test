from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("new_post/", views.new_post, name="new_post"),
]