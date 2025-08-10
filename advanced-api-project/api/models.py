from django.db import models
from datetime import date

class Author(models.Model):
    """
    Author model to store details about a book's author.
    One author can have multiple books (one-to-many).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model representing a literary work.
    Linked to Author via a ForeignKey.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
