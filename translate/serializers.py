from rest_framework import serializers
from .models import Consult, Hashtag, LatestUpdate, OurOffer, Service, Industry, Review, FAQ, Language, Order, User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_superuser']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('This username already exists', code='409')
        return value

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        email = validated_data.pop('email')
        user = User.objects.create(username=validated_data['username'],
                                   first_name=first_name,
                                   last_name=last_name, email=email)
        user.set_password(validated_data['password'])
        user.save()
        return user


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
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


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
        

class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'
