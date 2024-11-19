from django.urls import path
from .views import PromotionListView, PromotionCreateView

urlpatterns = [
    path('', PromotionCreateView.as_view(), name='promotion-initilize'),
    path('<int:pk>/', PromotionListView.as_view(), name='promotion-list'),
]
