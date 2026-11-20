from modeltranslation.translator import TranslationOptions, translator

from .models import (
    Category,
    CoatLength,
    CoatType,
    Country,
    NativeLanguage,
    Dogs,
    Section,
    Temperament,
)


class DogsTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "varieties",
        "colors",
        "summary",
        "history",
        "care",
        "good_fit",
        "think_twice",
        "daily_life",
        "quirks",
    )


class CountryTranslationOptions(TranslationOptions):
    fields = ("name",)


class NativeLanguageTranslationOptions(TranslationOptions):
    fields = ("name",)


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "desc", "short_desc")


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
translator.register(NativeLanguage, NativeLanguageTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Section, SectionTranslationOptions)
translator.register(CoatType, CoatTypeTranslationOptions)
translator.register(CoatLength, CoatLengthTranslationOptions)
translator.register(Temperament, TemperamentTranslationOptions)
