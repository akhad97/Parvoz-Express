from .models import LandingData
from modeltranslation.translator import TranslationOptions, translator


class LandingDataTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


translator.register(LandingData, LandingDataTranslationOptions)
