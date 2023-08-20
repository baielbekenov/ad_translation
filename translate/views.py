from rest_framework import generics

from translate.models import Hashtag
from translate.serializers import HashtagSerializer
# Create your views here.


class HashtagListAPIView(generics.ListAPIView):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all().order_by('-id')