from django.db import models
from products.models import Product
from django.utils.timezone import now

class Promotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='promotions')
    discount_percentage = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    class Meta:
        db_table = 'promotions'

    def is_active(self):
        return self.start_date <= now() <= self.end_date

    def __str__(self):
        return f"{self.product.name} - {self.discount_percentage}%"
    