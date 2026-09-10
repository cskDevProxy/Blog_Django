from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post
from .models import News
from .models import PostFile


# Главная страница
def index(request):
    posts = Post.objects.filter(status='published').order_by("-created_date")
    return render(request, "blog/index.html", {"posts": posts})

# Развёрнутая запись
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    return render(request, 'blog/post_detail.html', {'post':post})

# Новые записи(5 штук)
def new_post(request):
    posts = Post.objects.filter(status='published').order_by("-created_date")[:5]
    return render(request, "blog/new_post.html", {'posts': posts})

# О создателе
def creator(request):
    return render(request, "blog/сreator.html")

# Новости
def news(request):
    news = News.objects.all().order_by("-news_date")[:5]
    return render(request, 'blog/news.html', {'news':news})

