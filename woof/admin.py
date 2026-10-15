from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import (
    Dogs,
    Category,
    Country,
    DogImage,
    Section,
    CoatType,
    CoatLength,
    Temperament,
    ConsentLog,
)


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


class DogsAdminForm(forms.ModelForm):
    """Force English labels in the country dropdown.

    By default Django renders the related object with ``__str__``, which
    follows the admin UI language; here we always want the English name
    so the picker stays predictable regardless of the admin language.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field = self.fields.get("country")
        if field:
            field.label_from_instance = lambda obj: obj.name_en or obj.name

    class Meta:
        model = Dogs
        fields = "__all__"


@admin.register(Dogs)
class DogsAdmin(admin.ModelAdmin):
    form = DogsAdminForm
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
        "history",
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
        "title_uk",
        "title_es",
        "slug",
        "cat",
        "section",
        "varieties",
        "varieties_ru",
        "varieties_de",
        "varieties_it",
        "varieties_sr_latn",
        "varieties_uk",
        "varieties_es",
        "country",
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
        "colors_uk",
        "colors_es",
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
        "summary_uk",
        "summary_es",
        "history",
        "history_ru",
        "history_de",
        "history_it",
        "history_sr_latn",
        "history_uk",
        "history_es",
        "care",
        "care_ru",
        "care_de",
        "care_it",
        "care_sr_latn",
        "care_uk",
        "care_es",
        "living_conditions",
        "living_conditions_ru",
        "living_conditions_de",
        "living_conditions_it",
        "living_conditions_sr_latn",
        "living_conditions_uk",
        "living_conditions_es",
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


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "sort_order",
        "name",
        "name_ru",
        "name_de",
        "name_it",
        "name_sr_latn",
    )
    list_display_links = ("name",)
    search_fields = ("name", "name_ru")
    ordering = ("sort_order", "name")

    fields = (
        "name",
        "name_en",
        "name_ru",
        "name_de",
        "name_it",
        "name_sr_latn",
        "name_uk",
        "name_es",
        "sort_order",
    )


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
        "name_uk",
        "name_es",
        "desc",
        "desc_ru",
        "desc_de",
        "desc_it",
        "desc_sr_latn",
        "desc_uk",
        "desc_es",
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

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn", "name_uk", "name_es", "category")


@admin.register(CoatType)
class CoatTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn", "name_uk", "name_es")


@admin.register(CoatLength)
class CoatLengthAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn", "name_uk", "name_es")


@admin.register(Temperament)
class TemperamentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn", "name_uk", "name_es")


admin.site.site_title = "Woof Dogs admin"
admin.site.site_header = "Woof Dogs admin"


@admin.register(ConsentLog)
class ConsentLogAdmin(admin.ModelAdmin):
    """Read-only register of cookie-banner decisions (Art. 7 GDPR)."""

    list_display = (
        "created_at",
        "action",
        "analytics",
        "notice_version",
        "consent_id",
        "page",
    )
    list_filter = ("action", "analytics")
    search_fields = ("consent_id",)
    readonly_fields = ("created_at",)
    list_per_page = 50
    date_hierarchy = "created_at"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
