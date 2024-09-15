from django.contrib import admin
from .models import Developer, SubDeveloper


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'time_create', 'is_published', 'slug']
    list_editable = ['content', 'is_published', 'slug']
    search_fields = ['lesson']


@admin.register(SubDeveloper)
class SubDeveloperAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'slug']
    list_editable = ['content', 'slug']
    search_fields = ['lesson']



