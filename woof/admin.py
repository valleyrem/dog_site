from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Dogs, Category, DogImage, Section, CoatType, CoatLength


class DogImageInline(admin.TabularInline):
    model = DogImage
    extra = 4
    readonly_fields = ('preview',)
    fields = ('image', 'author', 'preview')

    def preview(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='80'>")
        return "—"

    preview.short_description = "Preview"


@admin.register(Dogs)
class DogsAdmin(admin.ModelAdmin):
    inlines = [DogImageInline]

    list_display = (
        'title',
        'get_html_photo',
        'country',
        'is_published',
        'id',
    )

    list_display_links = ('id', 'title')
    filter_horizontal = ('coat_length', 'coat_type' )

    search_fields = (
        'title',
        'summary',
        'care',
        'living_conditions',
        'colors',
        'life_expectancy',
        'height',
        'weight',
    )

    list_editable = ('is_published',)

    list_filter = (
        'cat',
        'size',
        'family_friendliness',
        'hypoallergenic',
        'is_published',
        'time_create',
    )

    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    ordering = ('title',)

    fields = (
        # main
        'title',
        'slug',
        'cat',
        'section',
        'varieties',
        'country',

        # photo
        'photo',
        'photo_author',
        'get_html_photo',

        # characteristics
        'life_expectancy',
        'size',
        'height',
        'weight',
        'coat_length',
        'coat_type',
        'colors',
        'trainability',
        'activity_level',
        'barking_level',
        'family_friendliness',
        'hypoallergenic',

        # description
        'summary',
        'care',
        'living_conditions',

        # general
        'is_published',
        'time_create',
        'time_update',
    )

    readonly_fields = (
        'time_create',
        'time_update',
        'get_html_photo',
    )

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='60'>")
        return "No image"

    get_html_photo.short_description = "Cover"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','fci_number' ,'name', 'group_preview', 'desc')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

    readonly_fields = ('group_preview',)

    def group_preview(self, obj):
        if obj.group_image:
            return mark_safe(
                f'<img src="{obj.group_image.url}" width="120" style="object-fit: cover;">'
            )
        return "—"

    group_preview.short_description = 'Preview'


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    search_fields = ('name',)


def __str__(self):
    return self.name


@admin.register(CoatType)
class CoatTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(CoatLength)
class CoatLengthAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.site_title = 'Woof Dogs admin'
admin.site.site_header = 'Woof Dogs admin'
