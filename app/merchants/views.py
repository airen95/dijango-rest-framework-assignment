from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Merchant
from .serializers import MerchantSerializer
from rest_framework.permissions import IsAuthenticated


class MerchantCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    
class MerchantDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
