from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.post.models import Post


# Create your views here.
class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        query = get_object_or_404(self.model, slug=slug)
        context = super().get_context_data()
        context['post'] = query
        return context
    # def patch():