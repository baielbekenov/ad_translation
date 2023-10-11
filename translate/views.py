from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Consult, Freelancer, LatestUpdate, OurOffer, Service, Industry, Review, FAQ, Language, Order
from .serializers import ConsultSerializer, FreelancerSerializer, LatestUpdateSerializer, OurOfferSerializer, ServiceSerializer, \
    IndustrySerializer, ReviewSerializer, FAQSerializer, LanguageSerializer, OrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.utils import translation


# ///////////////////////////////////////////////////////
# This views is created for create operations in models


class FAQCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class ConsultcreateView(generics.CreateAPIView):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer 
    
    
class FreelancerCreateView(generics.CreateAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer



# ///////////////////////////////////////////////////////

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class LatestUpdateListAPIView(generics.ListAPIView):
    queryset = LatestUpdate.objects.all()
    serializer_class = LatestUpdateSerializer
    
    def get_queryset(self):
        queryset = LatestUpdate.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class OurOfferListView(generics.ListAPIView):
    queryset = OurOffer.objects.all()
    serializer_class = OurOfferSerializer
    
    def get_queryset(self):
        queryset = OurOffer.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        queryset = Service.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class IndustryListView(generics.ListAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    
    def get_queryset(self):
        queryset = Industry.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = Review.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class FAQListView(APIView):

    def get(self, request, *args, **kwargs):
        faq = FAQ.objects.all()
        serializers = FAQSerializer(faq, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        queryset = FAQ.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class LanguageListView(APIView):

    def get(self, request, *args, **kwargs):
        language = Language.objects.all()
        serializers = LanguageSerializer(language, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        queryset = Language.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset
    

class ConsultListView(APIView):
    
    def get(self, request, *args, **kwargs):
        consult = Consult.objects.all()
        serializers = ConsultSerializer(consult, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    

class FreelancerListView(APIView):
    
    def get(self, request, *args, **kwargs):
        freelancer = Freelancer.objects.all()
        serializers = FreelancerSerializer(freelancer, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    
# --------------------------------------------


class LanguageRetrieveView(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    

class IndustryDetailView(generics.RetrieveAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    


