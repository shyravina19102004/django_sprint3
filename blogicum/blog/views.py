from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone

POSTS_PER_PAGE = 5

def index(request):
    """Главная страница с последними опубликованными постами."""
    template = 'blog/index.html'
    post_list = Post.objects.get_published_posts()[:POSTS_PER_PAGE]
    context = {'post_list': post_list}
    return render(request, template, context)

def post_detail(request, id):
    """Отображает детальную информацию о посте."""
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related('author', 'category', 'location'),
        pk=id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {'post': post}
    return render(request, template, context)

def category_posts(request, category_slug):
    """Отображает все посты определенной категории."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = category.posts.get_published_posts()
    context = {'post_list': post_list, 'category_slug': category_slug}
    return render(request, template, context)