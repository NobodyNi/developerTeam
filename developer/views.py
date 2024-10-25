from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView

from .services import random_lesson_slug

from developer.models import Category, Developer, CategoryOOP, SubDeveloper, SubCategoryOOP, SubCategoryAlgoritm, \
    CategoryAlgoritm, CategoryAsync, SubCategoryAsync
from .utils import PostMixin, SlugMappingMixin


class IndexView(TemplateView):
    template_name = 'developer/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_theme'] = random_lesson_slug()
        return context


class DirectionView(SlugMappingMixin, View):
    def get(self, request, dir_slug):
        category = get_object_or_404(Category, slug=dir_slug)
        model = self.slug_to_model.get(dir_slug)
        if model is None:
            return HttpResponse('Страница не найдена')

        posts = model.objects.filter(is_published=1).order_by('time_create')
        template_name = self.slug_to_template[dir_slug]

        context = {
            'title': category.direction,
            'posts': posts
        }

        return render(request, template_name, context=context)


class PostView(PostMixin, ListView):
    model = Developer
    template_name = 'developer/post.html'
    lesson_attr = 'sub_lesson'
    slug_field = 'post_slug'


class SubPostView(PostMixin, ListView):
    model = SubDeveloper
    template_name = 'developer/post.html'
    slug_field = 'sub_slug'


class PostViewOOP(PostMixin, ListView):
    model = CategoryOOP
    template_name = 'developer/post_oop.html'
    lesson_attr = 'sub_lesson_oop'
    slug_field = 'cat_oop_slug'


class SubPostViewOOP(PostMixin, ListView):
    model = SubCategoryOOP
    template_name = 'developer/post_oop.html'
    slug_field = 'sub_slug'


class PostViewAlgoritm(PostMixin, ListView):
    model = CategoryAlgoritm
    template_name = 'developer/post_algoritm.html'
    lesson_attr = 'sub_lesson_algoritm'
    slug_field = 'algoritm_slug'


class SubPostViewAlgoritm(PostMixin, ListView):
    model = SubCategoryAlgoritm
    template_name = 'developer/post_algoritm.html'
    slug_field = 'sub_algoritm'


class PostViewAsync(PostMixin, ListView):
    model = CategoryAsync
    template_name = 'developer/post_async.html'
    lesson_attr = 'sub_lesson_async'
    slug_field = 'async_slug'


class SubPostViewAsync(PostMixin, ListView):
    model = SubCategoryAsync
    template_name = 'developer/post_async.html'
    slug_field = 'sub_async'
