from rest_framework import serializers
from .models import Hashtag, LatestUpdate, OurOffer, Service, Industry, Review, FAQ, Language


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class LatestUpdateSerializer(serializers.ModelSerializer):
    hashtag = HashtagSerializer(many=True)

    class Meta:
        model = LatestUpdate
        fields = '__all__'


class OurOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurOffer
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'