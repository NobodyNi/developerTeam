from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from developer.models import Category, Developer, CategoryOOP, SubDeveloper, SubCategoryOOP


# menu = [{'title': 'Главная страница', 'url_name': 'home'},
#         {'title': 'О сайте', 'url_name': 'about'}]


def index(request):
    return render(request, 'developer/index.html')


# def about(request):
#     data = {
#         'title': 'О сайте',
#         'menu': menu,
#     }
#     return render(request, 'developer/about.html', context=data)


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
    elif dir_slug == 'python-async':
        return render(request, 'developer/async_py.html')
    else:
        return HttpResponse('Страница не найдена')


def show_post(request, post_slug):
    posts = get_object_or_404(Developer, slug=post_slug)
    lesson = posts.sub_lesson.all()
    data = {
        'title': posts.lesson,
        'posts': posts,
        'lesson': lesson,
    }
    return render(request, 'developer/post.html', context=data)


def show_post_oop(request, cat_oop_slug):
    posts = get_object_or_404(CategoryOOP, slug=cat_oop_slug)
    lesson = posts.sub_lesson_oop.all()
    data = {
        'title': posts.lesson,
        'posts': posts,
        'lesson': lesson,
    }
    return render(request, 'developer/post_oop.html', context=data)


def show_sub_lesson(request, sub_slug):
    lesson = get_object_or_404(SubDeveloper, slug=sub_slug)
    data = {
        'title': lesson.lesson,
        'posts': lesson,
    }
    return render(request, 'developer/post.html', context=data)


def show_sub_lesson_oop(request, sub_slug):
    lesson = get_object_or_404(SubCategoryOOP, slug=sub_slug)
    data = {
        'title': lesson.lesson,
        'posts': lesson,
    }
    return render(request, 'developer/post_oop.html', context=data)
