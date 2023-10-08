from django.urls import path
from .views import ConsultListView, ConsultcreateView, FreelancerCreateView, FreelancerListView, HashtagCreateView, IndustryDetailView, LatestUpdateCreateView, OurOfferCreateView, ServiceCreateView, IndustryCreateView, \
    ReviewCreateView, FAQCreateView, HashtagListView, OurOfferListView, ServiceListView, \
    IndustryListView, ReviewListView, FAQListView, LanguageListView, OrderCreateView, OrderListView, RegisterView, \
    LogoutView, LoginView, LatestUpdateListAPIView, LanguageRetrieveView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('hashtags/create/', HashtagCreateView.as_view(), name='hashtag-create'),
    path('latest_updates/create/', LatestUpdateCreateView.as_view(), name='latest-update-create'),
    path('our_offers/create/', OurOfferCreateView.as_view(), name='our-offer-create'),
    path('services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('industries/create/', IndustryCreateView.as_view(), name='industry-create'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('faq/create/', FAQCreateView.as_view(), name='faq-     '),
    path('consult/create/', ConsultcreateView.as_view(), name='consult-create'),
    path('freelance/create/', FreelancerCreateView.as_view(), name='freelance-crate'),

    path('hashtags/list/', HashtagListView.as_view(), name='hashtag-list'),
    path('latest_updates/list/', LatestUpdateListAPIView.as_view(), name='latest-update-list'),
    path('language/list/', LanguageListView.as_view(), name='language_list'),
    path('our_offers/list/', OurOfferListView.as_view(), name='our-offer-list'),
    path('services/list/', ServiceListView.as_view(), name='service-list'),
    path('industries/list/', IndustryListView.as_view(), name='industry-list'),
    path('reviews/list/', ReviewListView.as_view(), name='review-list'),
    path('order/list/', OrderListView.as_view(), name='order-list'),
    path('faq/list/', FAQListView.as_view(), name='faq-list'),
    path('consult/list/', ConsultListView.as_view(), name='consult-list'),
    path('freelance/list/', FreelancerListView.as_view(), name='freelance-list'),
    
    path('detailed/industries/<int:pk>/', IndustryDetailView.as_view(), name='industry_detail'),
    path('detailed/languages/<int:pk>/', LanguageRetrieveView.as_view(), name='language_detail')
]