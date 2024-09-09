from django.shortcuts import render, get_object_or_404

from developer.models import Category

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'}]


def index(request):
    data = {
        'title': 'Главная страница',
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
    data = {
        'title': category.direction,
    }
    return render(request, 'developer/post.html', context=data)
