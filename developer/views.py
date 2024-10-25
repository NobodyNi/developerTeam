from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView

from .services import random_lesson_slug

from developer.models import Category, Developer, CategoryOOP, SubDeveloper, SubCategoryOOP, SubCategoryAlgoritm, \
    CategoryAlgoritm, CategoryAsync, SubCategoryAsync
from .utils import PostMixin


class IndexView(TemplateView):
    template_name = 'developer/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_theme'] = random_lesson_slug()
        return context


class DirectionView(View):
    def get(self, request, dir_slug):
        category = get_object_or_404(Category, slug=dir_slug)

        if dir_slug == 'python':
            posts = Developer.objects.filter(is_published=1).order_by('time_create')
            template_name = 'developer/category.html'
        elif dir_slug == 'python-oop':
            posts = CategoryOOP.objects.filter(is_published=1).order_by('time_create')
            template_name = 'developer/category_oop.html'
        elif dir_slug == 'python-async':
            posts = CategoryAsync.objects.filter(is_published=1).order_by('time_create')
            template_name = 'developer/async_py.html'
        elif dir_slug == 'python-algoritm':
            posts = CategoryAlgoritm.objects.filter(is_published=1).order_by('time_create')
            template_name = 'developer/algoritm_py.html'
        else:
            return HttpResponse('Страница не найдена')

        context = {
            'title': category.direction,
            'posts': posts
        }

        return render(request, template_name, context=context)


class PostView(PostMixin, ListView):
    model = Developer
    template_name = 'developer/post.html'
    lesson_attr = 'sub_lesson'

    def get_queryset(self):
        post_slug = self.kwargs['post_slug']
        return [get_object_or_404(Developer, slug=post_slug)]


class SubPostView(PostMixin, ListView):
    model = SubDeveloper
    template_name = 'developer/post.html'

    def get_queryset(self):
        sub_slug = self.kwargs['sub_slug']
        return [get_object_or_404(SubDeveloper, slug=sub_slug)]


class PostViewOOP(PostMixin, ListView):
    model = CategoryOOP
    template_name = 'developer/post_oop.html'
    lesson_attr = 'sub_lesson_oop'

    def get_queryset(self):
        cat_oop_slug = self.kwargs['cat_oop_slug']
        return [get_object_or_404(CategoryOOP, slug=cat_oop_slug)]


class SubPostViewOOP(PostMixin, ListView):
    model = SubCategoryOOP
    template_name = 'developer/post_oop.html'

    def get_queryset(self):
        sub_slug = self.kwargs['sub_slug']
        return [get_object_or_404(SubCategoryOOP, slug=sub_slug)]


class PostViewAlgoritm(PostMixin, ListView):
    model = CategoryAlgoritm
    template_name = 'developer/post_algoritm.html'
    lesson_attr = 'sub_lesson_algoritm'

    def get_queryset(self):
        algoritm_slug = self.kwargs['algoritm_slug']
        return [get_object_or_404(CategoryAlgoritm, slug=algoritm_slug)]


class SubPostViewAlgoritm(PostMixin, ListView):
    model = SubCategoryAlgoritm
    template_name = 'developer/post_algoritm.html'

    def get_queryset(self):
        sub_algoritm = self.kwargs['sub_algoritm']
        return [get_object_or_404(SubCategoryAlgoritm, slug=sub_algoritm)]


class PostViewAsync(PostMixin, ListView):
    model = CategoryAsync
    template_name = 'developer/post_async.html'
    lesson_attr = 'sub_lesson_async'

    def get_queryset(self):
        async_slug = self.kwargs['async_slug']
        return [get_object_or_404(CategoryAsync, slug=async_slug)]


class SubPostViewAsync(PostMixin, ListView):
    model = SubCategoryAsync
    template_name = 'developer/post_async.html'

    def get_queryset(self):
        sub_async = self.kwargs['sub_async']
        return [get_object_or_404(SubCategoryAsync, slug=sub_async)]
