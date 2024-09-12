from django.contrib import admin
from .models import Developer


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'time_create', 'is_published', 'slug']
    list_display_links = ['lesson']
    list_editable = ['content']



