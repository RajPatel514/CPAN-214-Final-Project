from django.db import models
from django.contrib.auth.models import User

class BookManager(models.Manager):
    def get_all_books(self):
        return self.all()

    def get_book(self, id):
        return self.get(id=id)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    objects = BookManager()

    def __str__(self):
        return f"{self.title} by {self.author}"
