from modeltranslation.translator import translator, TranslationOptions
from symposion.sponsorship.models import Sponsor, SponsorLevel

class SponsorI18n(TranslationOptions):
    fields = ('name', 'annotation',)
translator.register(Sponsor, SponsorI18n)


class SponsorLevelI18n(TranslationOptions):
    fields = ('name',)
translator.register(SponsorLevel, SponsorLevelI18n)
