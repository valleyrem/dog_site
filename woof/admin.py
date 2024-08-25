from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class WoofAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'title', 'size', 'coat_type', 'trainability', 'activity_level', 'time_create', 'get_html_photo',
    'is_published')
    list_display_links = ('id', 'title')
    search_fields = (
    'title', 'content', 'size', 'coat_type', 'care', 'living_conditions', 'trainability', 'activity_level')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'size', 'coat_type', 'trainability', 'activity_level')
    prepopulated_fields = {"slug": ("title",)}
    fields = (
        'title', 'slug', 'cat', 'content', 'size', 'coat_type', 'care', 'living_conditions',
        'trainability', 'activity_level', 'photo', 'get_html_photo', 'is_published',
        'time_create', 'time_update'
    )
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    ordering = ('-time_create',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Miniature"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Dogs)
class DogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_email', 'slug', 'size', 'coat_type', 'is_published')  # Выберите поля для отображения
    search_fields = ('title', 'user_email')  # Поля для поиска
    list_filter = ('size', 'coat_type', 'is_published')  # Фильтрация по полям

admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Woof Dogs admin'
admin.site.site_header = 'Woof Dogs admin'
