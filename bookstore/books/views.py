from django.shortcuts import render, redirect
from .models import Book

def delete_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == "POST":
        book.delete()
        return redirect('/')

    return render(request, 'books/delete.html', {'book': book})

def edit_book(request, id):
    book = Book.objects.get(id=id)

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
            description=description
        )

        return redirect('/')
    return render(request, 'books/add.html')


def homepage(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def book_detail(request, id):
    return render(request, 'books/detail.html')

def homepage(request):
    books = Book.objects.get_all_books()
    return render(request, 'books/home.html', {'books': books})
