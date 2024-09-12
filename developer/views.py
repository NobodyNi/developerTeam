from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from developer.models import Category, Developer, CategoryOOP

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'}]


def index(request):
    data = {
        'menu': menu,
    }
    return render(request, 'developer/index.html', context=data)


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'developer/about.html', context=data)


def show_direction(request, dir_slug):
    category = get_object_or_404(Category, slug=dir_slug)
    data_1 = {
        'title': category.direction,
        'posts': Developer.objects.filter(is_published=1),
    }

    data_2 = {
        'title': category.direction,
        'posts': CategoryOOP.objects.filter(is_published=1),
    }

    if dir_slug == 'python':
        return render(request, 'developer/category.html', context=data_1)
    elif dir_slug == 'python-oop':
        return render(request, 'developer/category_oop.html', context=data_2)
    else:
        return HttpResponse('Страница не найдена')


def show_post(request, post_slug):
    posts = get_object_or_404(Developer, slug=post_slug)
    data = {
        'title': posts.lesson,
        'posts': posts,
    }
    return render(request, 'developer/post.html', context=data)
