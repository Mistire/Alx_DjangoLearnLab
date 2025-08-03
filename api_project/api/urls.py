from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books')

urlpatterns = [
  path('books/', BookList.as_view(), name='books-list'),
  path('', include(router.urls))
]