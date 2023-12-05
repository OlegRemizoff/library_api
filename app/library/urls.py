from django.urls import path
from .views import BookListAPIView, BookCreateAPIView ,BookRetrieveUpdateDestroyAPIView
from .views import UserListAPIView, UserCreateAPIView




urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-change'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
]