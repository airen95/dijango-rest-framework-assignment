from rest_framework import generics
from .models import Keyword
from .serializers import KeywordSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# List, Create Hashtag
class KeywordListView(generics.ListCreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    
    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAuthenticated()]
        return [AllowAny()]


# Retrieve, Update, and Delete Hashtag
class KeywordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]
