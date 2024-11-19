from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from .models import User
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from users.models import User
from merchants.models import Merchant
from merchants.serializers import MerchantSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetailsView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        merchant = Merchant.objects.filter(user_id=user_id).first()  # Retrieve the merchant linked to the user
        merchant_serializer = MerchantSerializer(merchant) if merchant else None
        
        return Response({
            "user": serializer.data,
            "merchant": merchant_serializer.data if merchant_serializer else None,
        }, status=status.HTTP_200_OK)
        