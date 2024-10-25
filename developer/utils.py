from django.shortcuts import get_object_or_404

from developer.models import Developer, CategoryOOP, CategoryAsync, CategoryAlgoritm


class PostMixin:
    lesson_attr = None

    def get_queryset(self):
        slug_field = self.slug_field
        slug = self.kwargs[slug_field]
        return [get_object_or_404(self.model, slug=slug)]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object_list[0]
        context['title'] = post.lesson
        context['posts'] = post
        if self.lesson_attr:
            context['lesson'] = getattr(post, self.lesson_attr).all().order_by('pk')
        return context


class SlugMappingMixin:
    slug_to_model = {
        'python': Developer,
        'python-oop': CategoryOOP,
        'python-async': CategoryAsync,
        'python-algoritm': CategoryAlgoritm
    }

    slug_to_template = {
        'python': 'developer/category.html',
        'python-oop': 'developer/category_oop.html',
        'python-async': 'developer/async_py.html',
        'python-algoritm': 'developer/algoritm_py.html'
    }
