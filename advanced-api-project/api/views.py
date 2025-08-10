from rest_framework import generics, permissions

from api.permissions import ReadOnlyOrAuthenticated
from .models import Book
from .serializers import BookSerializer
from api import serializers


class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    Returns details for a specific book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [ReadOnlyOrAuthenticated]

    def perform_create(self, serializer):
        """
        Save the new book instance with validated data.
        Additional logic (e.g., attaching request.user) can go here.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [ReadOnlyOrAuthenticated]

    def perform_update(self, serializer):
      instance = serializer.save()
      if instance.publication_year > 2025:
        raise serializers.ValidationError("Year cannot be in the future.")


class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [ReadOnlyOrAuthenticated]



