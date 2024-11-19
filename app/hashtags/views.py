from rest_framework import generics
from .models import Hashtag
from .serializers import HashtagSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
    
# List, Create Hashtag
class HashtagListView(generics.ListCreateAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    
    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAuthenticated()]
        return [AllowAny()]


# Retrieve, Update, and Delete Hashtag
class HashtagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]
