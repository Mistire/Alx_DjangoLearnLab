from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=100)

  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"{self.name}"

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

  def __init__(self, title, author):
    self.title = title
    self.author = author


  def __str__(self):
    return f"{self.title} by {self.author}"

class Library(models.Model):
  name = models.CharField(max_length=100)
  book = models.ManyToManyField(Book)

class Librarian(models.Model):
  name = models.CharField(max_length=100)
  library = models.OneToOneField(Library, on_delete=models.CASCADE)