from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hashtag, LatestUpdate, OurOffer, Service, Industry, Review, FAQ
from .serializers import HashtagSerializer, LatestUpdateSerializer, OurOfferSerializer, ServiceSerializer, \
    IndustrySerializer, ReviewSerializer, FAQSerializer


# ///////////////////////////////////////////////////////
# This views is created for create operations in models


class HashtagCreateView(APIView):
    def post(self, request, format=None):
        serializer = HashtagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LatestUpdateCreateView(APIView):
    def post(self, request, format=None):
        serializer = LatestUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OurOfferCreateView(APIView):
    def post(self, request, format=None):
        serializer = OurOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceCreateView(APIView):
    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndustryCreateView(APIView):
    def post(self, request, format=None):
        serializer = IndustrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewCreateView(APIView):
    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FAQCreateView(APIView):
    def post(self, request, format=None):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ///////////////////////////////////////////////////////


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


class OurOfferListView(APIView):
    def get(self, request, *args, **kwargs):
        ourOffer = OurOffer.objects.all()
        serializers = OurOfferSerializer(ourOffer, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


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


class ReviewListView(APIView):
    def get(self, request, *args, **kwargs):
        review = Review.objects.all()
        serializers = ReviewSerializer(review, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class FAQListView(APIView):
    def get(self, request, *args, **kwargs):
        faq = FAQ.objects.all()
        serializers = FAQSerializer(faq, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)





