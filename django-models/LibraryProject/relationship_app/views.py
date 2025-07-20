from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to a page of your choice
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class BookListView(ListView):
  model = Book
  template_name = 'relationship_app/list_book.html'
  context_object_name = 'book'

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'




# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'relationship_app/register.html'
#     success_url = reverse_lazy('login') 


class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'


class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'



# --- Role check functions ---
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# --- Role-based views ---
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

