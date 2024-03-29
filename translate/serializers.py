from django.conf import settings
from rest_framework import serializers
from .models import Consult, DetailIndustry, DetailLanguage, Freelancer, Hashtag, LatestUpdate,  OurOffer, Service, Industry, Review, FAQ, Language, Order


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'
        
 
class DetailLanguageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DetailLanguage
        fields = '__all__' 


class LanguageSerializer(serializers.ModelSerializer):
    detaillanguage = DetailLanguageSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Language
        fields = '__all__'
        
    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.img.url) if obj.img else None
        

class DetailIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailIndustry
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
    detailindustry = DetailIndustrySerializer(many=True, read_only=True)
    
    class Meta:
        model = Industry
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        
    
    def validate(self, data):
        type_file = data.get('type_file')
        documents = data.get('documents')
        link = data.get('link')

        if type_file == Order.LINK:
            if not link:
                raise serializers.ValidationError({'link': 'This field is required when type_file is Link.'})
            data.pop('documents', None)  # Удалить documents, если оно присутствует
        else:
            if not documents:
                raise serializers.ValidationError({'documents': 'This field is required when type_file is Documents, Video, or Audio.'})
            data.pop('link', None)  # Удалить link, если он присутствует

        return data
    

class FreelancerSerializer(serializers.ModelSerializer):
    language1 = serializers.PrimaryKeyRelatedField(many=True, queryset=Language.objects.all())
    language2 = serializers.PrimaryKeyRelatedField(many=True, queryset=Language.objects.all())

    class Meta:
        model = Freelancer
        fields = '__all__'
        
    
    def create(self, validated_data):
        language1_data = validated_data.pop('language1')
        language2_data = validated_data.pop('language2')

        freelancer = Freelancer.objects.create(**validated_data)
        freelancer.language1.set(language1_data)
        freelancer.language2.set(language2_data)

        return freelancer
        


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
        

class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'
