from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .services import random_lesson_slug

from developer.models import Category, Developer, CategoryOOP, SubDeveloper, SubCategoryOOP, SubCategoryAlgoritm, \
    CategoryAlgoritm, CategoryAsync, SubCategoryAsync


# menu = [{'title': 'Главная страница', 'url_name': 'home'},
#         {'title': 'О сайте', 'url_name': 'about'}]


def index(request):
    data = {
        'random_theme': random_lesson_slug(),
    }
    return render(request, 'developer/index.html', context=data)


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
        'posts': Developer.objects.filter(is_published=1).order_by('time_create'),
    }

    data_2 = {
        'title': category.direction,
        'posts': CategoryOOP.objects.filter(is_published=1).order_by('time_create'),
    }

    data_3 = {
        'title': category.direction,
        'posts': CategoryAlgoritm.objects.filter(is_published=1).order_by('time_create'),
    }

    data_4 = {
        'title': category.direction,
        'posts': CategoryAsync.objects.filter(is_published=1).order_by('time_create'),
    }

    if dir_slug == 'python':
        return render(request, 'developer/category.html', context=data_1)
    elif dir_slug == 'python-oop':
        return render(request, 'developer/category_oop.html', context=data_2)
    elif dir_slug == 'python-async':
        return render(request, 'developer/async_py.html', context=data_4)
    elif dir_slug == 'python-algoritm':
        return render(request, 'developer/algoritm_py.html', context=data_3)
    else:
        return HttpResponse('Страница не найдена')


def show_post(request, post_slug):
    posts = get_object_or_404(Developer, slug=post_slug)
    lesson = posts.sub_lesson.all().order_by('pk')
    data = {
        'title': posts.lesson,
        'posts': posts,
        'lesson': lesson,
    }
    return render(request, 'developer/post.html', context=data)


def show_post_oop(request, cat_oop_slug):
    posts = get_object_or_404(CategoryOOP, slug=cat_oop_slug)
    lesson = posts.sub_lesson_oop.all().order_by('pk')
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


def show_post_algoritm(request, algoritm_slug):
    posts = get_object_or_404(CategoryAlgoritm, slug=algoritm_slug)
    lesson = posts.sub_lesson_algoritm.all().order_by('pk')
    data = {
        'title': posts.lesson,
        'posts': posts,
        'lesson': lesson,
    }
    return render(request, 'developer/post_algoritm.html', context=data)


def show_sub_lesson_algoritm(request, sub_algoritm):
    lesson = get_object_or_404(SubCategoryAlgoritm, slug=sub_algoritm)
    data = {
        'title': lesson.lesson,
        'posts': lesson,
    }
    return render(request, 'developer/post_algoritm.html', context=data)


def show_post_async(request, async_slug):
    posts = get_object_or_404(CategoryAsync, slug=async_slug)
    lesson = posts.sub_lesson_async.all().order_by('pk')
    data = {
        'title': posts.lesson,
        'posts': posts,
        'lesson': lesson,
    }
    return render(request, 'developer/post_async.html', context=data)


def show_sub_lesson_async(request, sub_async):
    lesson = get_object_or_404(SubCategoryAsync, slug=sub_async)
    data = {
        'title': lesson.lesson,
        'posts': lesson,
    }
    return render(request, 'developer/post_async.html', context=data)
