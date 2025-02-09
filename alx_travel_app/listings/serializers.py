"""
    Serializers for the listing and booking models
"""

from rest_framework import serializers
from .models import Listing, Booking, Payment


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["payment_reference", "tel", "email", "amount", "status"]
        read_only_fields = ["status"]
            
