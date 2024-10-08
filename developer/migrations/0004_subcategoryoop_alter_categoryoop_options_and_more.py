# Generated by Django 4.2.1 on 2024-09-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0003_alter_developer_options_alter_subdeveloper_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoryOOP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(max_length=100, verbose_name='Подтема')),
                ('content', models.TextField(blank=True, verbose_name='Информация')),
                ('slug', models.SlugField(max_length=125, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Подтема ооп',
                'verbose_name_plural': 'Подтемы ооп',
            },
        ),
        migrations.AlterModelOptions(
            name='categoryoop',
            options={'verbose_name': 'ООП', 'verbose_name_plural': 'ООП'},
        ),
        migrations.AddField(
            model_name='categoryoop',
            name='sub_lesson_oop',
            field=models.ManyToManyField(blank=True, related_name='sub_opp', to='developer.subcategoryoop'),
        ),
    ]
