from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=100)

  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

  class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

  # def __init__(self, title, author):
  #   self.title = title
  #   self.author = author


  # def __str__(self):
  #   return f"{self.title} by {self.author}"

class Library(models.Model):
  library_name = models.CharField(max_length=100)
  book = models.ManyToManyField(Book)

class Librarian(models.Model):
  librarian_name = models.CharField(max_length=100)
  library = models.OneToOneField(Library, on_delete=models.CASCADE)



class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"