# Generated by Django 4.2.1 on 2024-09-10 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0003_developer_direct'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOOP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=125, unique=True)),
            ],
        ),
    ]