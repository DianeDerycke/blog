from django.shortcuts import render
from blog.models import Category
from django.views.generic.list import ListView

# Create your views here.
class PostListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Context is ===> ")
        print(context)
        return context
