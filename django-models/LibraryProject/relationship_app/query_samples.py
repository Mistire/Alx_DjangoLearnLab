from django.shortcuts import get_object_or_404
from .models import Author, Book, Librarian, Library

# books_by_author = Book.objects.filter(field_name='author')
# list_books = Library.objects.get(name=Library.name)
# get_librariyan = Librarian.objects.filter(field_name='library')


def get_books_by_author(name):
  author = Author.objects.get(Author, name=name)
  return Book.objects.filter(author=author)

def get_books_by_library(library_name):
  library = Library.objects.get(name=library_name)
  return library.books.all()

def get_librarian_by_library(library_name):
  library = Library.objects.get(name=library_name)
  return library.librarian