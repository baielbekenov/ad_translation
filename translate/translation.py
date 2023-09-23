from modeltranslation.translator import translator, TranslationOptions
from .models import Language, LatestUpdate, OurOffer, Service, Industry, Review, FAQ


class LanguageTranslationOptions(TranslationOptions):
    fields = ('name',)
    
class LatestUpdateTranslationOptions(TranslationOptions):
    fields = ('title', 'iconText', 'text', 'icon')
    

class OurOfferTranslationOptions(TranslationOptions):
    fields = ('miniText', 'title')
    

class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
    
    
class IndustryTranslationOptions(TranslationOptions):
    fields = ('iconText', 'text')
    

class ReviewTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )   


class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


translator.register(Language, LanguageTranslationOptions)
translator.register(LatestUpdate, LatestUpdateTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(Review, ReviewTranslationOptions)
translator.register(Industry, IndustryTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
translator.register(OurOffer, OurOfferTranslationOptions)
