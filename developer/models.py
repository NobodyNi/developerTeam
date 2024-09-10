from django.db import models
from django.urls import reverse


class Developer(models.Model):
    lesson = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=125, unique=True, db_index=True)

    direct = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.lesson


class Category(models.Model):
    direction = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self):
        return self.direction

    def get_absolute_url(self):
        return reverse('direction', kwargs={'dir_slug': self.slug})




