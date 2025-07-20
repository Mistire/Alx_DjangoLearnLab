from django.urls import path
from . import views
from .views import list_books, login_view, logout_view, register_view

urlpatterns = [
  path('register/', views.CreateView.as_view, name='register'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('logout/', views.LogoutView.as_view(), name='logout'),
  path('books_list/', list_books, name='books-list-c'),
  path('book_list_c/', views.BookListView.as_view(), name='book-list-c'),
  path('library_detail/', views.LibraryDetailView.as_view(), name='library-detail'),
]