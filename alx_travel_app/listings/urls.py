from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, InitiatePaymentView, VerifyPaymentView

router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('pay/', InitiatePaymentView.as_view(), name='initiate-payment'),
    path('pay/verify/<str:tx_ref>/', VerifyPaymentView.as_view(), name='verify-payment')
] + router.urls
