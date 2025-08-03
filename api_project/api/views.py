# Token-based authentication is enabled in settings.py
# All BookViewSet actions require an authenticated user
# Token can be retrieved at /api/token/ by POSTing username and password



from django.shortcuts import render

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class BookList(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]