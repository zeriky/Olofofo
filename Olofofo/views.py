from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


def index_list(request):
    a_list = Post.objects.filter(status=1).order_by('-created_on')
    query = request.GET.get("q")
    if query:
        a_list = a_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    paginator = Paginator(a_list, 4)
    page = request.GET.get('page')
    try:
        a = paginator.page(page)
    except PageNotAnInteger:
        a = paginator.page(1)
    except EmptyPage:
        a = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'a_list': a})


def news_list(request):
    b_list = Post.objects.filter(category=0, status=1).order_by('-created_on')
    paginator = Paginator(b_list, 4)
    page = request.GET.get('page')
    try:
        b = paginator.page(page)
    except PageNotAnInteger:
        b = paginator.page(1)
    except EmptyPage:
        b = paginator.page(paginator.num_pages)
    return render(request, 'news.html', {'b_list': b})


def entertainment_list(request):
    c_list = Post.objects.filter(status=1, category=1).order_by('-created_on')
    paginator = Paginator(c_list, 4)
    page = request.GET.get('page')
    try:
        c = paginator.page(page)
    except PageNotAnInteger:
        c = paginator.page(1)
    except EmptyPage:
        c = paginator.page(paginator.num_pages)
    return render(request, 'entertainment.html', {'c_list': c})


def sports_list(request):
    d_list = Post.objects.filter(status=1, category=2).order_by('-created_on')
    paginator = Paginator(d_list, 4)
    page = request.GET.get('page')
    try:
        d = paginator.page(page)
    except PageNotAnInteger:
        d = paginator.page(1)
    except EmptyPage:
        d = paginator.page(paginator.num_pages)
    return render(request, 'sports.html', {'d_list': d})


def world_news_list(request):
    e_list = Post.objects.filter(status=1, category=3).order_by('-created_on')
    paginator = Paginator(e_list, 4)
    page = request.GET.get('page')
    try:
        e = paginator.page(page)
    except PageNotAnInteger:
        e = paginator.page(1)
    except EmptyPage:
        e = paginator.page(paginator.num_pages)
    return render(request, 'world_news.html', {'e_list': e})


def post_details_view(request, slug):
    q = get_object_or_404(Post, slug=slug)
    return render(request, 'post_details.html', {'q': q})
