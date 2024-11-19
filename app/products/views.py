from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer, ProductPromotionActiveSerializer
from promotions.models import Promotion
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny


# List, Create Product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAuthenticated()]
        return [AllowAny()]

# Retrieve, Update, and Delete Product
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
# Search Products by Category
class ProductsByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(categories__id=category_id)
    
# Search Products by Hashtag:
class ProductsByHashtagView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        hashtag_id = self.kwargs['hashtag_id']
        return Product.objects.filter(hashtags__id=hashtag_id)
    
# Search Products have most similar keywords:
class ProductsByKeywordView(APIView):
    """
    Fetch products that match or are similar to a given keyword.
    """

    def get(self, request, keyword):
        # Case-insensitive and partial matches
        products = Product.objects.filter(
            Q(name__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(keywords__name__icontains=keyword)
        ).distinct()

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Retrieve Products have active promotions:
class ActivePromotionsView(generics.ListAPIView):
    serializer_class = ProductPromotionActiveSerializer

    def get_queryset(self):
        return Promotion.objects.filter(
            start_date__lte=now(), 
            end_date__gte=now()
        ).order_by('-discount_percentage')
