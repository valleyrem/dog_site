from modeltranslation.translator import TranslationOptions, translator

from .models import Category, CoatLength, CoatType, Dogs, Section, Temperament


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


class CoatTypeTranslationOptions(TranslationOptions):
    fields = ("name",)


class CoatLengthTranslationOptions(TranslationOptions):
    fields = ("name",)


class TemperamentTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Dogs, DogsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Section, SectionTranslationOptions)
translator.register(CoatType, CoatTypeTranslationOptions)
translator.register(CoatLength, CoatLengthTranslationOptions)
translator.register(Temperament, TemperamentTranslationOptions)