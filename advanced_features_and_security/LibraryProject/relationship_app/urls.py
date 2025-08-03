from django.urls import path

from .admin_view import admin_dashboard
from .librarian_view import librarian_dashboard
from .member_view import member_dashboard
from . import views
from .views import list_books, register
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
  path('register/', views.register, name='register'),
  path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
  path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
  path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
  path('librarian/dashboard/', librarian_dashboard, name='librarian-dashboard'),
  path('member/dashboard/', member_dashboard, name='member-dashboard'),
  path('books_list/', list_books, name='books-list-c'),
  path('book_list_c/', views.BookListView.as_view(), name='book-list-c'),
  path('library_detail/', views.LibraryDetailView.as_view(), name='library-detail'),
  path('add_book/', views.add_book, name='add-book'),
  path('books/<int:pk>/edit_book/', views.edit_book, name='edit-book'),
  path('books/<int:pk>/delete_book/', views.delete_book, name='delete-book'),
]