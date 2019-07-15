from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from blog.category.models import Category

# Create your views here.
class PostFromCategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        query = get_object_or_404(self.model, slug=slug)
        context = super().get_context_data(**kwargs)
        context['posts'] = query.posts.all()
        return context