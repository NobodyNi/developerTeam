from django.contrib import admin
from .models import Developer, SubDeveloper, CategoryOOP, SubCategoryOOP, CategoryAlgoritm, SubCategoryAlgoritm, \
    CategoryAsync, SubCategoryAsync


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'time_create', 'is_published', 'slug']
    list_editable = ['content', 'is_published', 'slug']
    search_fields = ['lesson']
    list_per_page = 5


@admin.register(SubDeveloper)
class SubDeveloperAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'slug']
    list_editable = ['content', 'slug']
    search_fields = ['lesson']
    list_per_page = 5
    fields = ['lesson', 'content', 'slug']


@admin.register(CategoryOOP)
class CategoryOOPAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'time_create', 'is_published', 'slug']
    list_editable = ['content', 'is_published', 'slug']
    search_fields = ['lesson']
    list_per_page = 5


@admin.register(SubCategoryOOP)
class SubCategoryOOPAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'slug']
    list_editable = ['content', 'slug']
    search_fields = ['lesson']
    list_per_page = 5
    fields = ['lesson', 'content', 'slug']


@admin.register(CategoryAlgoritm)
class CategoryAlgoritmAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'time_create', 'is_published', 'slug']
    list_editable = ['content', 'is_published', 'slug']
    search_fields = ['lesson']
    list_per_page = 5


@admin.register(SubCategoryAlgoritm)
class SubCategoryAlgoritmAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'slug']
    list_editable = ['content', 'slug']
    search_fields = ['lesson']
    list_per_page = 5
    fields = ['lesson', 'content', 'slug']


@admin.register(CategoryAsync)
class CategoryAsyncAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'time_create', 'is_published', 'slug']
    list_editable = ['content', 'is_published', 'slug']
    search_fields = ['lesson']
    list_per_page = 5


@admin.register(SubCategoryAsync)
class SubCategoryAsyncAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'content', 'slug']
    list_editable = ['content', 'slug']
    search_fields = ['lesson']
    list_per_page = 5
    fields = ['lesson', 'content', 'slug']