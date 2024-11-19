from rest_framework import generics
from .models import Promotion
from .serializers import PromotionSerializer
from rest_framework.permissions import IsAuthenticated

class PromotionCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    
class PromotionListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
