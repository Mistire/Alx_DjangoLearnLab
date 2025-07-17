from django.urls import path
from . import views

urlpatterns = [
  path('books_list_func/', views.list_book_with_author, name='books-list-c'),
  path('book_list_class/', views.BookListView.as_view(), name='book-list-c'),
  path('library_detail/', views.LibraryDetailView.as_view(), name='library-detail'),
]