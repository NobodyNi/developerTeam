# Generated by Django 4.2.1 on 2024-09-22 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0002_subdeveloper_developer_sub_lesson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='developer',
            options={'ordering': ['time_create'], 'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
        migrations.AlterModelOptions(
            name='subdeveloper',
            options={'verbose_name': 'Подтема', 'verbose_name_plural': 'Подтемы'},
        ),
        migrations.AlterField(
            model_name='developer',
            name='content',
            field=models.TextField(blank=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='lesson',
            field=models.CharField(max_length=100, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='slug',
            field=models.SlugField(max_length=125, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='subdeveloper',
            name='content',
            field=models.TextField(blank=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='subdeveloper',
            name='lesson',
            field=models.CharField(max_length=100, verbose_name='Подтема'),
        ),
        migrations.AlterField(
            model_name='subdeveloper',
            name='slug',
            field=models.SlugField(max_length=125, unique=True, verbose_name='Слаг'),
        ),
    ]