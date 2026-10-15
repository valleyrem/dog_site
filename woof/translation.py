from modeltranslation.translator import TranslationOptions, translator

from .models import (
    Category,
    CoatLength,
    CoatType,
    Country,
    Dogs,
    Section,
    Temperament,
)


class DogsTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "varieties",
        "life_expectancy",
        "height",
        "weight",
        "colors",
        "summary",
        "history",
        "care",
        "living_conditions",
        "photo_author",
    )


class CountryTranslationOptions(TranslationOptions):
    fields = ("name",)


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "desc")


class SectionTranslationOptions(TranslationOptions):
    fields = ("name",)


class CoatTypeTranslationOptions(TranslationOptions):
    fields = ("name",)


class CoatLengthTranslationOptions(TranslationOptions):
    fields = ("name",)


class TemperamentTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Dogs, DogsTranslationOptions)
translator.register(Country, CountryTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Section, SectionTranslationOptions)
translator.register(CoatType, CoatTypeTranslationOptions)
translator.register(CoatLength, CoatLengthTranslationOptions)
translator.register(Temperament, TemperamentTranslationOptions)
