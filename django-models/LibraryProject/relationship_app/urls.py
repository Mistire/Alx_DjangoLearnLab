from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
  path('books_list/', list_books, name='books-list-c'),
  path('book_list_c/', views.BookListView.as_view(), name='book-list-c'),
  path('library_detail/', views.LibraryDetailView.as_view(), name='library-detail'),
]