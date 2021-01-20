from django.shortcuts import render

from library.models import Book


def view_index(request):
    books = Book.objects.all()
    return render(
        request, 'pages/index.html', {'books': books})
