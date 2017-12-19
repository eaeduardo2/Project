from django.shortcuts import render
from .models import Post
from django.contrib.postgres.search import SearchQuery

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'info/list.html', {'posts': posts})

def search(request):
    return SearchQuery(search)