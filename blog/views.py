from urllib.parse import urlencode
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Count, Q

from .models import Post, News, Tegi


def page_window(current, total, radius=2):
    """Список номеров страниц: первая, последняя, окрестность текущей, '…' на разрывах."""
    if total <= 7:
        return list(range(1, total + 1))
    
    around = [p for p in range(current - radius, current + radius + 1)
              if 1 < p < total]
    pages = [1] + around + [total]
    result = []
    
    for p in pages:
        if result and p - result[-1] > 1:
            result.append('…')
        result.append(p)
    
    return result

def index(request, tag_id=None):
    selected_tag = tag_id.strip() if tag_id else ''

    posts = Post.objects.filter(status='published')
    if selected_tag:
        posts = posts.filter(tegs__name=selected_tag).distinct()
    posts = posts.order_by('-created_date', '-id')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except (EmptyPage, InvalidPage):
        raise Http404('Такой страницы нет')
    except InvalidPage:
        page_obj = paginator.page(1)

    tags = (
        Tegi.objects
        .annotate(post_count=Count('posts', filter=Q(posts__status='published')))
        .filter(post_count__gt=0)
        .order_by('-post_count', 'name')
    )

    context = {
        'page_obj': page_obj,
        'page_window': page_window(page_obj.number, paginator.num_pages),
        'tags': tags,
        'selected_tag': selected_tag,
        
    }

    return render(request, "blog/index.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    
    prev_post = Post.objects.filter(
        status='published', created_date__lt=post.created_date
    ).order_by('-created_date', '-id').first()
    
    next_post = Post.objects.filter(
        status='published', created_date__gt=post.created_date
    ).order_by('created_date', 'id').first()
    
    return render(request, 'blog/post_detail.html',
                  {'post': post, 'prev_post': prev_post, 'next_post': next_post})


def new_post(request):
    posts = Post.objects.filter(status='published').order_by("-created_date")[:5]
    return render(request, "blog/new_post.html", {'posts': posts})


def creator(request):
    return render(request, "blog/creator.html")  


def news(request):
    news_items = News.objects.all().order_by("-news_date")[:5]
    return render(request, 'blog/news.html', {'news': news_items})