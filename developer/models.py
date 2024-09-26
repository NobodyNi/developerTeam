from django.db import models
from django.urls import reverse


class Developer(models.Model):
    lesson = models.CharField(max_length=100, verbose_name='Тема')
    content = models.TextField(blank=True, verbose_name='Информация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Статус')
    slug = models.SlugField(max_length=125, unique=True, db_index=True, verbose_name='Слаг')

    direct = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    sub_lesson = models.ManyToManyField('SubDeveloper', blank=True, related_name='sub')

    def __str__(self):
        return self.lesson

    def get_absolute_url(self):
        return reverse('posting', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ['time_create']
        verbose_name = 'Python'
        verbose_name_plural = 'Python'


class SubDeveloper(models.Model):
    lesson = models.CharField(max_length=100, verbose_name='Подтема')
    content = models.TextField(blank=True, verbose_name='Информация')
    slug = models.SlugField(max_length=125, db_index=True, unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.lesson

    def get_absolute_url(self):
        return reverse('sub_lesson', kwargs={'sub_slug': self.slug})

    class Meta:
        verbose_name = 'Python подтема'
        verbose_name_plural = 'Python подтемы'


class Category(models.Model):
    direction = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self):
        return self.direction

    def get_absolute_url(self):
        return reverse('direction', kwargs={'dir_slug': self.slug})

    class Meta:
        ordering = ['id']


class CategoryOOP(models.Model):
    lesson = models.CharField(max_length=100, verbose_name='Тема')
    content = models.TextField(blank=True, verbose_name='Информация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Статус')
    slug = models.SlugField(max_length=125, unique=True, db_index=True, verbose_name='Слаг')

    sub_lesson_oop = models.ManyToManyField('SubCategoryOOP', blank=True, related_name='sub_opp')

    def __str__(self):
        return self.lesson

    def get_absolute_url(self):
        return reverse('posting_oop', kwargs={'cat_oop_slug': self.slug})

    class Meta:
        verbose_name = "ООП"
        verbose_name_plural = "ООП"


class SubCategoryOOP(models.Model):
    lesson = models.CharField(max_length=100, verbose_name='Подтема')
    content = models.TextField(blank=True, verbose_name='Информация')
    slug = models.SlugField(max_length=125, db_index=True, unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.lesson

    def get_absolute_url(self):
        return reverse('sub_lesson_oop', kwargs={'sub_slug': self.slug})

    class Meta:
        verbose_name = 'ООП подтема'
        verbose_name_plural = 'ООП подтемы'