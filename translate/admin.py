from django.contrib import admin

from translate.models import Hashtag, LatestUpdate, OurOffer, Service, \
    Industry, Review, FAQ, Language, Order, Consult

# Register your models here.

admin.site.register(Hashtag)
admin.site.register(LatestUpdate)
admin.site.register(OurOffer)
admin.site.register(Service)
admin.site.register(Language)
admin.site.register(Industry)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(FAQ)
admin.site.register(Consult)
