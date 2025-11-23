from django.shortcuts import render
from .models import Book

def homepage(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def book_detail(request, id):
    return render(request, 'books/detail.html')
