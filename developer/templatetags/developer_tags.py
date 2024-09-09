from django import template

from developer.models import Category

register = template.Library()


@register.inclusion_tag('developer/list_direction.html')
def get_direction():
    cats = Category.objects.all()
    return {'cats': cats}

