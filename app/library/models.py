from django.db import models
from django.utils import timezone
from .tasks import send_email


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):  
        send_email.delay(self.email, 'Thank you for registering!')
        return super().save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    author = models.CharField(max_length=100, verbose_name="Автор")
    publication_year = models.IntegerField(verbose_name="Год публикации")
    isbn = models.IntegerField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
