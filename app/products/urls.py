from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # put, post, delete
    path('search-by-category/<int:category_id>', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('search-by-hashtag/<int:hashtag_id>', ProductsByHashtagView.as_view(), name='products-by-hashtag'),
    path('search-by-keywords/<str:keyword>', ProductsByKeywordView.as_view(), name='products-by-keywords'),
    path('active-promotion', ActivePromotionsView.as_view(), name='products-have-promotion'),
]
