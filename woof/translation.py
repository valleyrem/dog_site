from modeltranslation.translator import TranslationOptions, translator

from .models import Category, Dogs, Section


class DogsTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "varieties",
        "country",
        "life_expectancy",
        "height",
        "weight",
        "colors",
        "summary",
        "care",
        "living_conditions",
        "photo_author",
    )


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "desc")


class SectionTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Dogs, DogsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Section, SectionTranslationOptions)