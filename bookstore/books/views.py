from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import login 
from .serializers import BookSerializer
from rest_framework.decorators import api_view  
from rest_framework.response import Response 

def delete_book(request, id):
    book = Book.objects.get(id=id)

    if book.posted_by != request.user:
        return render(request, 'books/forbidden.html')

    if request.method == "POST":
        book.delete()
        return redirect('/')

    return render(request, 'books/delete.html', {'book': book})

def logout_user(request):
    logout(request)
    return redirect('/')

def edit_book(request, id):
    book = Book.objects.get(id=id)

    if book.posted_by is None:
        book.posted_by = request.user
        book.save()

    if book.posted_by != request.user:
        return render(request, 'books/forbidden.html')

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        rating = request.POST.get('rating')
        description = request.POST.get('description')

        errors = []

        if not title:
            errors.append("Title is required.")
        if not author:
            errors.append("Author is required.")
        if not year:
            errors.append("Year is required.")
        if not rating:
            errors.append("Rating is required.")
        if not description:
            errors.append("Description is required.")

        if errors:
            return render(request, 'books/edit.html', {
                'errors': errors,
                'book': book,
                'title': title,
                'author': author,
                'year': year,
                'rating': rating,
                'description': description,
            })

        book.title = title
        book.author = author
        book.year = year
        book.rating = rating
        book.description = description
        book.save()

        return redirect('/')

    return render(request, 'books/edit.html', {'book': book})


@login_required
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        rating = request.POST.get('rating')
        description = request.POST.get('description')

        errors = []

        if not title:
            errors.append("Title is required.")
        if not author:
            errors.append("Author is required.")
        if not year:
            errors.append("Year is required.")
        if not rating:
            errors.append("Rating is required.")
        if not description:
            errors.append("Description is required.")

        if errors:
            return render(request, 'books/add.html', {
                'errors': errors,
                'title': title,
                'author': author,
                'year': year,
                'rating': rating,
                'description': description,
            })

        Book.objects.create(
            title=title,
            author=author,
            year=year,
            rating=rating,
            description=description,
            posted_by=request.user 
        )

        return redirect('/')

    return render(request, 'books/add.html')



def homepage(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/detail.html', {'book': book})


def homepage(request):
    books = Book.objects.get_all_books()
    return render(request, 'books/home.html', {'books': books})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        errors = []

        if password1 != password2:
            errors.append("Passwords don't match")
        if User.objects.filter(username=username).exists():
            errors.append("Username taken")
        
        if errors:
            return render(request, 'books/register.html', {'errors': errors})

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)  
        return redirect('/')

    return render(request, 'books/register.html')


@api_view(['GET'])
def api_get_books(request):
    """Get all books as JSON"""
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_get_book(request, id):
    """Get single book by ID as JSON"""
    try:
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)