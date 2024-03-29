"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from blog.post.views import PostListView
from blog.post.views import PostDetailView
from blog.category.views import PostFromCategoryListView

urlpatterns = [
    path('post/<slug>', PostDetailView.as_view(), name='post-detail'),
    path('category/<slug>', PostFromCategoryListView.as_view(), name='post-list'),
    path('posts/', PostListView.as_view(), name='post-list'),
]