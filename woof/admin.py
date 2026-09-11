from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Dogs, Category, DogImage, Section, CoatType, CoatLength, Temperament


class DogImageInline(admin.TabularInline):
    model = DogImage
    extra = 4
    readonly_fields = ("preview",)
    fields = ("image", "author", "preview")

    def preview(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='80'>")
        return "—"

    preview.short_description = "Preview"


@admin.register(Dogs)
class DogsAdmin(admin.ModelAdmin):
    inlines = [DogImageInline]

    list_display = (
        "title",
        "get_html_photo",
        "country",
        "is_published",
        "id",
    )

    list_display_links = ("id", "title")
    filter_horizontal = ("coat_length", "coat_type", "temperament")

    search_fields = (
        "title",
        "summary",
        "care",
        "living_conditions",
        "colors",
        "life_expectancy",
        "height",
        "weight",
    )

    list_editable = ("is_published",)

    list_filter = (
        "cat",
        "size",
        "family_friendliness",
        "hypoallergenic",
        "is_published",
        "time_create",
    )

    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    ordering = ("title",)

    fields = (
        # main
        "title",
        "title_ru",
        "title_de",
        "title_it",
        "title_sr_latn",
        "slug",
        "cat",
        "section",
        "varieties",
        "varieties_ru",
        "varieties_de",
        "varieties_it",
        "varieties_sr_latn",
        "country",
        "country_ru",
        "country_de",
        "country_it",
        "country_sr_latn",
        # photo
        "photo",
        "photo_author",
        "get_html_photo",
        # characteristics
        "life_expectancy",
        "size",
        "height",
        "weight",
        "coat_length",
        "coat_type",
        "temperament",
        "colors",
        "colors_ru",
        "colors_de",
        "colors_it",
        "colors_sr_latn",
        "trainability",
        "activity_level",
        "barking_level",
        "family_friendliness",
        "hypoallergenic",
        # description
        "summary",
        "summary_ru",
        "summary_de",
        "summary_it",
        "summary_sr_latn",
        "care",
        "care_ru",
        "care_de",
        "care_it",
        "care_sr_latn",
        "living_conditions",
        "living_conditions_ru",
        "living_conditions_de",
        "living_conditions_it",
        "living_conditions_sr_latn",
        # general
        "is_published",
        "time_create",
        "time_update",
    )

    readonly_fields = (
        "time_create",
        "time_update",
        "get_html_photo",
    )

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='60'>")
        return "No image"

    get_html_photo.short_description = "Cover"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "fci_number", "name", "group_preview", "desc")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    readonly_fields = ("group_preview",)

    fields = (
        "name",
        "name_ru",
        "name_de",
        "name_it",
        "name_sr_latn",
        "desc",
        "desc_ru",
        "desc_de",
        "desc_it",
        "desc_sr_latn",
        "fci_number",
        "slug",
        "group_image",
        "group_preview",
    )

    def group_preview(self, obj):
        if obj.group_image:
            return mark_safe(
                f'<img src="{obj.group_image.url}" width="120" style="object-fit: cover;">'
            )
        return "—"

    group_preview.short_description = "Preview"


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_display_links = ("id", "name")
    list_filter = ("category",)
    search_fields = ("name",)

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn", "category")


@admin.register(CoatType)
class CoatTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn")


@admin.register(CoatLength)
class CoatLengthAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn")


@admin.register(Temperament)
class TemperamentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn")


admin.site.site_title = "Woof Dogs admin"
admin.site.site_header = "Woof Dogs admin"
