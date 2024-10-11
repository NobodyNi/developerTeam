import random

from developer.models import SubDeveloper


def random_lesson_slug():
    lessons = SubDeveloper.objects.values_list('lesson', 'slug')
    if lessons:
        theme_lesson = random.choice(list(lessons))
    else:
        theme_lesson = None
    return theme_lesson


