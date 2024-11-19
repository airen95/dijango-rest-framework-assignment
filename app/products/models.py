from django.db import models
from merchants.models import Merchant
from categories.models import Category
from hashtags.models import Hashtag
from keywords.models import Keyword


class Product(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # # Many-to-Many Relationships
    categories = models.ManyToManyField(Category, related_name='products', blank=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='products', blank=True)
    keywords = models.ManyToManyField(Keyword, related_name='products', blank=True)
    
    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return self.name