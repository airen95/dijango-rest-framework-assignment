from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list-create'), # get, post
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),  # put, patch, delete
]
