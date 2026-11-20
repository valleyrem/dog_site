from django.contrib import admin
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from modeltranslation.admin import TabbedTranslationAdmin

from .models import (
    Dogs,
    Category,
    Country,
    NativeLanguage,
    DogImage,
    Section,
    CoatType,
    CoatLength,
    Temperament,
    ConsentLog,
    ContactMessage,
)


class DogImageInline(admin.TabularInline):
    model = DogImage
    extra = 4

    def get_extra(self, request, obj=None, **kwargs):
        # a new breed gets four empty slots; an existing one only needs a
        # single slot for the next photo
        return 1 if obj and obj.pk else self.extra

    readonly_fields = ("preview",)
    fields = ("image", "author", "preview")

    def preview(self, obj):
        if obj.image:
            return format_html("<img src='{}' width='80' alt=''>", obj.image.url)
        return "—"

    preview.short_description = "Preview"


LIFE_TOPICS = {
    "en": [
        "Walks",
        "Being alone",
        "At home",
        "Children",
        "Other animals",
        "Play and activities",
        "Daily routine",
    ],
    "ru": [
        "Прогулки",
        "Одиночество",
        "Дома",
        "Дети",
        "Другие животные",
        "Игры и занятия",
        "Распорядок дня",
    ],
    "de": [
        "Spaziergänge",
        "Alleinsein",
        "Zu Hause",
        "Kinder",
        "Andere Tiere",
        "Spiel und Beschäftigung",
        "Tagesablauf",
    ],
    "it": [
        "Passeggiate",
        "Da solo",
        "In casa",
        "Bambini",
        "Altri animali",
        "Gioco e attività",
        "Routine quotidiana",
    ],
    "es": [
        "Paseos",
        "Quedarse solo",
        "En casa",
        "Niños",
        "Otros animales",
        "Juegos y actividades",
        "Rutina diaria",
    ],
    "sr_latn": [
        "Šetnje",
        "Boravak sam",
        "Kod kuće",
        "Deca",
        "Druge životinje",
        "Igra i aktivnosti",
        "Dnevna rutina",
    ],
}


def life_placeholder(lang):
    """The usual topics, one per paragraph, as a hint in an empty field."""
    return "\n\n".join(f"{topic}: ..." for topic in LIFE_TOPICS[lang])


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
        for name, life in self.fields.items():
            if name == "daily_life" or name.startswith("daily_life_"):
                lang = name[len("daily_life_") :] or "en"
                life.widget.attrs["placeholder"] = life_placeholder(lang)

    class Meta:
        model = Dogs
        # the ModelAdmin below owns the field list; this form only overrides
        # how the related country is labelled
        fields = ()


@admin.register(Dogs)
class DogsAdmin(TabbedTranslationAdmin):
    form = DogsAdminForm
    inlines = [DogImageInline]
    change_form_template = "woof/admin/dog_change_form.html"

    list_display = (
        "title",
        "get_html_photo",
        "summary",
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
        "colors",
        "life_expectancy",
        "height_male",
        "height_female",
        "weight_male",
        "weight_female",
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

    # translated fields are listed once, by their base name: modeltranslation
    # turns each one into a row of language tabs
    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    "title",
                    "slug",
                    "cat",
                    "section",
                    "varieties",
                    "country",
                    "native_name",
                    "native_language",
                    "fci_standard",
                    "is_published",
                ),
            },
        ),
        (
            "Photo",
            {"fields": ("photo", "photo_author", "get_html_photo")},
        ),
        (
            "Texts",
            {
                "fields": (
                    "summary",
                    "history",
                    "daily_life",
                    "quirks",
                    "care",
                    "good_fit",
                    "think_twice",
                ),
            },
        ),
        (
            "Characteristics",
            {
                "classes": ("collapse",),
                "fields": (
                    "life_expectancy",
                    "size",
                    "height_male",
                    "height_female",
                    "weight_male",
                    "weight_female",
                    "coat_length",
                    "coat_type",
                    "temperament",
                    "colors",
                    "trainability",
                    "activity_level",
                    "barking_level",
                    "family_friendliness",
                    "hypoallergenic",
                    "prey_drive",
                ),
            },
        ),
        (
            "Dates",
            {
                "classes": ("collapse",),
                "fields": ("time_create", "time_update"),
            },
        ),
    )

    readonly_fields = (
        "time_create",
        "time_update",
        "get_html_photo",
    )

    def neighbours(self, obj):
        """The breeds before and after this one, in the order of the list."""
        ids = list(Dogs.objects.order_by("title", "pk").values_list("pk", flat=True))
        at = ids.index(obj.pk)
        prev_id = ids[at - 1] if at > 0 else None
        next_id = ids[at + 1] if at + 1 < len(ids) else None
        found = Dogs.objects.in_bulk([i for i in (prev_id, next_id) if i])
        return found.get(prev_id), found.get(next_id)

    def render_change_form(
        self, request, context, add=False, change=False, form_url="", obj=None
    ):
        context["show_save_and_add_another"] = False
        context["show_save_and_continue"] = False
        if change and obj is not None:
            context["prev_dog"], context["next_dog"] = self.neighbours(obj)
        return super().render_change_form(request, context, add, change, form_url, obj)

    def response_change(self, request, obj):
        for key, index in (("_save_prev", 0), ("_save_next", 1)):
            if key in request.POST:
                target = self.neighbours(obj)[index]
                if target is not None:
                    self.message_user(
                        request, f"{obj.title} was saved.", messages.SUCCESS
                    )
                    return HttpResponseRedirect(
                        reverse("admin:woof_dogs_change", args=[target.pk])
                    )
        return super().response_change(request, obj)

    def get_html_photo(self, obj):
        if obj.photo:
            return format_html("<img src='{}' width='60' alt=''>", obj.photo.url)
        return "No image"

    get_html_photo.short_description = "Cover"


@admin.register(NativeLanguage)
class NativeLanguageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "name_ru",
        "name_de",
        "name_it",
        "name_es",
        "name_sr_latn",
    )
    search_fields = ("name", "name_ru")
    ordering = ("name",)

    fields = (
        "name",
        "name_en",
        "name_ru",
        "name_de",
        "name_it",
        "name_es",
        "name_sr_latn",
    )


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
        "name_es",
        "sort_order",
    )


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ("id", "fci_number", "name", "short_desc")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    fields = (
        "name",
        "short_desc",
        "desc",
        "fci_number",
        "slug",
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # the one-sentence blurb gets a roomy box instead of a single line
        if db_field.name.startswith("short_desc"):
            kwargs["widget"] = forms.Textarea(attrs={"rows": 4, "cols": 80})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_display_links = ("id", "name")
    list_filter = ("category",)
    search_fields = ("name",)

    fields = (
        "name",
        "name_ru",
        "name_de",
        "name_it",
        "name_sr_latn",
        "name_es",
        "category",
    )


@admin.register(CoatType)
class CoatTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn", "name_es")


@admin.register(CoatLength)
class CoatLengthAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn", "name_es")


@admin.register(Temperament)
class TemperamentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

    fields = ("name", "name_ru", "name_de", "name_it", "name_sr_latn", "name_es")


CONTENT_MODELS = [
    "Dogs",
    "Category",
    "Section",
    "Country",
    "NativeLanguage",
    "CoatType",
    "CoatLength",
    "Temperament",
]
VISITOR_MODELS = ["ConsentLog", "ContactMessage"]


def get_app_list(request, app_label=None):
    """The breed catalogue first, visitor records after it, accounts last."""
    apps = admin.AdminSite.get_app_list(admin.site, request, app_label)
    result = []
    for app in apps:
        if app["app_label"] != "woof":
            continue
        by_name = {m["object_name"]: m for m in app["models"]}
        for title, names in (
            ("Dog catalogue", CONTENT_MODELS),
            ("Visitors", VISITOR_MODELS),
        ):
            models = [by_name.pop(n) for n in names if n in by_name]
            if models:
                result.append({**app, "name": title, "models": models})
        if by_name:  # anything registered later still shows up
            result.append({**app, "name": "Other", "models": list(by_name.values())})
    result.extend(app for app in apps if app["app_label"] != "woof")
    return result


admin.site.get_app_list = get_app_list
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


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Messages from the contact form: read and delete, never edit."""

    list_display = ("created_at", "email_or_dash", "short_message")
    search_fields = ("email", "message")
    readonly_fields = ("created_at", "email", "message")
    list_per_page = 50
    date_hierarchy = "created_at"

    @admin.display(description="E-mail", ordering="email")
    def email_or_dash(self, obj):
        return obj.email or "—"

    @admin.display(description="Message")
    def short_message(self, obj):
        text = " ".join(obj.message.split())
        return text if len(text) <= 100 else text[:100] + "…"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
