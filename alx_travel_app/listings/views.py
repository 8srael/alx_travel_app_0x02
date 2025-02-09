from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Listing, Booking, Payment, PaymentStatus
from .serializers import ListingSerializer, BookingSerializer, PaymentSerializer
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid


# Create your views here.

class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    

class InitiatePaymentView(APIView):
    def post(self, request):
    
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
        
            payment_reference = uuid.uuid4().hex     
            validated_data = serializer.validated_data 
                        
            # Prepare Chapa API request payload
            payload = {
                "amount": str(serializer.data["amount"]),
                "currency": "USD",
                # "email": serializer.data["email"],
                "tx_ref": payment_reference,
                "callback_url": f"{settings.SITE_URL}/api/pay/verify/"
            }

            headers = {
                "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
                "Content-Type": "application/json"
            }

            # Send request to Chapa API
            response = requests.post('https://api.chapa.co/v1/transaction/initialize', json=payload, headers=headers)
            chapa_response = response.json()
            
            print(chapa_response)

            if chapa_response.get("status") == "success":
                Payment.objects.create(
                                       payment_reference=payment_reference,
                                       tel=validated_data["tel"],
                                       email=validated_data["email"],
                                       amount=validated_data["amount"],
                                       status=PaymentStatus.PENDING
                                    )
                return Response({"message": "Payment initiated", "checkout_url": chapa_response["data"]["checkout_url"]}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Payment initiation failed"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPaymentView(APIView):
    def get(self, request, tx_ref):
        payment = get_object_or_404(Payment, payment_reference=tx_ref)

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.get(f"https://api.chapa.co/v1/transaction/verify/{tx_ref}", headers=headers)
        chapa_response = response.json()

        if chapa_response.get("status") == "success" and chapa_response["data"]["status"] == "success":
            payment.status = PaymentStatus.SUCCESS
            payment.save()
            return Response({"message": "Payment verified successfully"}, status=status.HTTP_200_OK)
        else:
            payment.status = PaymentStatus.FAILED
            payment.save()
            return Response({"error": "Payment verification failed"}, status=status.HTTP_400_BAD_REQUEST)
        
        

