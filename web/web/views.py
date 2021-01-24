from django.shortcuts import render

from library.models import Book, Category
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


def view_access(request):
    return render(request, 'auth/access.html')


@login_required()
def view_index(request):
    books = Book.objects.all()[::-1]

    return render(
        request, 'pages/index.html', {'books': books})


@login_required()
def view_post(request, book_id=None):
    book = None
    books = Book.objects.all()[:5]
    categories = Category.objects.all()

    try:
        book = Book.objects.get(id=book_id)
    except ObjectDoesNotExist:
        pass

    return render(
        request, 'pages/post-text.html', {'book': book, 'books': books, 'categories': categories})
