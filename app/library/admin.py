from django.contrib import admin
from .models import Book, User



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "isbn"]
    list_display_links = ["id", "title"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email"]
    list_display_links = ["id", "username"]
