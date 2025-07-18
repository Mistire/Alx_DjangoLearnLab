from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Book
from .models import Library

# Create your views here.

def list_books(request):
  books = Book.objects.all()
  return render(
    request, 
    'relationship_app/list_books.html', 
    {'book': books}
    )

class BookListView(ListView):
  model = Book
  template_name = 'relationship_app/list_book.html'
  context_object_name = 'book'

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'