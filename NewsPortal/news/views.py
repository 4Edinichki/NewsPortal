from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    model = Post
    ordering = 'id'
    template_name = 'news.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
