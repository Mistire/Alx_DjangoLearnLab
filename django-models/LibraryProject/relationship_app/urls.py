from django.urls import path
from . import views
from views import list_books_with_author, BookList, LibraryDetail

urlpatterns = [
  path('books_list_func/', list_books_with_author, name='books-list-c'),
  path('book_list_class/', views.BookListView.as_view(), name='book-list-c'),
  path('library_detail/', views.LibraryDetailView.as_view(), name='library-detail'),
]