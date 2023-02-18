from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Главная страница сайта
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    text = 'Главная страница проекта'
    title = 'Это главная страница проекта'
    context = {
        'posts': posts,
        'text': text,
        'title1': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'Старница с постами группы '
    text = 'Группа тайных поклонников графа'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
        'text': text,
    }
    return render(request, 'posts/group_list.html', context)
