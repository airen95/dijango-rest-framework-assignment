from django.urls import path
from .views import MerchantCreateView, MerchantDetailView

urlpatterns = [
    path('', MerchantCreateView.as_view(), name='merchant-create'),
    path('<int:pk>/', MerchantDetailView.as_view(), name='merchant-detail'),
]
