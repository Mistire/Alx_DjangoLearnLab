from django.db import models
from

# Create your models here.
class Book:
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  publication_date = models.DateField()