from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class WoofAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'title', 'size', 'coat_type', 'trainability', 'activity_level', 'coat_length', 'barking_level', 'time_create', 'get_html_photo',
    'is_published')
    list_display_links = ('id', 'title')
    search_fields = (
    'title', 'content', 'size', 'coat_type', 'care', 'living_conditions', 'trainability', 'activity_level')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'size', 'coat_type', 'trainability', 'activity_level')
    prepopulated_fields = {"slug": ("title",)}
    fields = (
        'title', 'slug', 'cat', 'content', 'size', 'coat_type', 'trainability', 'activity_level', 'coat_length', 'barking_level', 'care', 'living_conditions',
         'photo', 'get_html_photo', 'is_published',
        'time_create', 'time_update'
    )
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    ordering = ('-time_create',)

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50'>")
        else:
            return "No Image"

    get_html_photo.short_description = "Miniature"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Dogs)
class DogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user_email', 'is_published')
    search_fields = ('title', 'user_email')
    list_filter = ('cat', 'size', 'coat_type', 'is_published')

admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Woof Dogs admin'
admin.site.site_header = 'Woof Dogs admin'
