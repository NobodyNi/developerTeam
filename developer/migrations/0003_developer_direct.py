# Generated by Django 4.2.1 on 2024-09-09 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='direct',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='developer.category'),
        ),
    ]