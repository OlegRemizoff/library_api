from django.urls import path
from .views import BookListAPIView, BookCreateAPIView ,BookRetrieveUpdateDestroyAPIView




urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-change'),
]