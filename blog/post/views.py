from django.shortcuts import render
from blog.post.models import Post
from django.views.generic.list import ListView

# Create your views here.
class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context