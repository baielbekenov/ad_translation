from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from translate.models import Hashtag, LatestUpdate, OurOffer, Service, \
    Industry, Review, FAQ, Language, Order, Consult, Freelancer

# Register your models here.

class LatestUpdateAdmin(TranslationAdmin):
    pass


class OurOfferAdmin(TranslationAdmin):
    pass


class ServiceAdmin(TranslationAdmin):
    pass


class LanguageAdmin(TranslationAdmin):
    pass


class IndustryAdmin(TranslationAdmin):
    pass


class ReviewAdmin(TranslationAdmin):
    pass


class FAQAdmin(TranslationAdmin):
    pass



admin.site.register(Hashtag)
admin.site.register(LatestUpdate, LatestUpdateAdmin)
admin.site.register(OurOffer, OurOfferAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Consult)
admin.site.register(Freelancer)