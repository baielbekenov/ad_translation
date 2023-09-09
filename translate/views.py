from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .models import Hashtag, LatestUpdate, OurOffer, Service, Industry, Review, FAQ, Language, Order, User
from .serializers import HashtagSerializer, LatestUpdateSerializer, OurOfferSerializer, ServiceSerializer, \
    IndustrySerializer, ReviewSerializer, FAQSerializer, LanguageSerializers, OrderSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# ////////////////////////////////////////////////////////
# This section is created for registration, login, logout

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'status': 403,
                'errors': serializer.errors,
                'message': 'Something went wrong'
            })

        if User.objects.filter(username=serializer.validated_data['username']).exists():
            return Response({
                'error': 'This user already exists!'
            }, status=409)

        user = serializer.save()
        token_obj, _ = Token.objects.get_or_create(user=user)

        return Response({
            'status': 200,
            'payload': serializer.data,
            'token': str(token_obj),
            'is_superuser': user.is_superuser,
            'message': 'Your data is saved'
        })


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'errors': 'invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key, 'is_superuser': user.is_superuser},
                        status=status.HTTP_200_OK)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


# ///////////////////////////////////////////////////////
# This views is created for create operations in models


class HashtagCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = HashtagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LatestUpdateCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = LatestUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OurOfferCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = OurOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndustryCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = IndustrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FAQCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderCreateView(APIView):

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ///////////////////////////////////////////////////////

class OrderListView(APIView):

    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        serializers = OrderSerializer(order, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class HashtagListView(APIView):

    def get(self, request, *args, **kwargs):
        hashtag = Hashtag.objects.all()
        serializers = HashtagSerializer(hashtag, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class LatestUpdateListView(APIView):

    def get(self, request, *args, **kwargs):
        latestUpdate = LatestUpdate.objects.all()
        serializers = LatestUpdateSerializer(latestUpdate, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def get_image(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        return request.build_absolute_uri(image_url)


class OurOfferListView(APIView):

    def get(self, request, *args, **kwargs):
        ourOffer = OurOffer.objects.all()
        serializers = OurOfferSerializer(ourOffer, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def get_image(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        return request.build_absolute_uri(image_url)


class ServiceListView(APIView):

    def get(self, request, *args, **kwargs):
        service = Service.objects.all()
        serializers = ServiceSerializer(service, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class IndustryListView(APIView):

    def get(self, request, *args, **kwargs):
        industry = Industry.objects.all()
        serializers = IndustrySerializer(industry, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def get_image(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        return request.build_absolute_uri(image_url)


class ReviewListView(APIView):

    def get(self, request, *args, **kwargs):
        review = Review.objects.all()
        serializers = ReviewSerializer(review, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def get_image(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        return request.build_absolute_uri(image_url)


class FAQListView(APIView):

    def get(self, request, *args, **kwargs):
        faq = FAQ.objects.all()
        serializers = FAQSerializer(faq, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class LanguageListView(APIView):

    def get(self, request, *args, **kwargs):
        language = Language.objects.all()
        serializers = LanguageSerializers(language, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)




