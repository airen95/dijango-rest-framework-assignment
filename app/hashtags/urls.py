from django.urls import path
from .views import *

urlpatterns = [
    path('', HashtagListView.as_view(), name='hashtag-list'), # get, post
    path('<int:pk>/', HashtagDetailView.as_view(), name='hashtag-detail'),  # put, patch, delete
]
