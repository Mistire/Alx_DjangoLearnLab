from .models import Book, Librarian

books_by_author = Book.objects.filter(field_name='author')
list_books = Book.objects.all()
get_librariyan = Librarian.objects.filter(field_name='library')