from django.shortcuts import render

from library.models import Book, Category
from django.db.models import ObjectDoesNotExist


def view_index(request):
    books = Book.objects.all()
    return render(
        request, 'pages/index.html', {'books': books})


def view_post(request, id=None):
    book = None
    books = Book.objects.all()[:5]
    categories = Category.objects.all()

    try:
        book = Book.objects.get(id=id)
    except ObjectDoesNotExist:
        pass

    return render(
        request, 'pages/post-text.html', {'book': book, 'books': books, 'categories': categories})
