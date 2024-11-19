from django.urls import path
from .views import *

urlpatterns = [
    path('', KeywordListView.as_view(), name='hashtag-list'), # get, post
    path('<int:pk>/', KeywordDetailView.as_view(), name='hashtag-detail'),  # put, patch, delete
]
