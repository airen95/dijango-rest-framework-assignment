from rest_framework import serializers
from categories.serializers import  CategorySerializer
from keywords.serializers import KeywordSerializer
from promotions.serializers import PromotionSerializer
from promotions.models import Promotion
from hashtags.serializers import HashtagSerializer
from .models import Product
from categories.models import Category
from hashtags.models import Hashtag
from keywords.models import Keyword

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, required=False)
    hashtags = HashtagSerializer(many=True, required=False)
    keywords = KeywordSerializer(many=True, required=False)
    promotions = PromotionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'merchant', 'name', 'description', 'price', 'categories', 'hashtags', 'keywords', 'promotions']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        hashtags_data = validated_data.pop('hashtags', [])
        keywords_data = validated_data.pop('keywords', [])
        product = Product.objects.create(**validated_data)

        for category_data in categories_data:
            category, _ = Category.objects.get_or_create(**category_data)
            product.categories.add(category)

        for hashtag_data in hashtags_data:
            hashtag, _ = Hashtag.objects.get_or_create(**hashtag_data)
            product.hashtags.add(hashtag)

        for keyword_data in keywords_data:
            keyword, _ = Keyword.objects.get_or_create(**keyword_data)
            product.keywords.add(keyword)

        return product
    
class ProductPromotionActiveSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Promotion
        fields = ['id', 'product', 'discount_percentage', 'start_date', 'end_date', 'is_active']

    def get_is_active(self, obj):
        return obj.is_active()
