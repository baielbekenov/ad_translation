from django.urls import path
from translate import views

urlpatterns = [
    path('', views.HashtagListAPIView.as_view()),
]