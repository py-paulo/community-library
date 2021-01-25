from django.shortcuts import render

from library.models import Book, Category, Comment
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
    book, comments, raw_comments = None, {}, []

    books = Book.objects.all()[:5]
    categories = Category.objects.all()

    try:
        book = Book.objects.get(id=book_id)
    except ObjectDoesNotExist:
        pass
    else:
        raw_comments = Comment.objects.filter(approved=True).filter(author=book.owner)

    for comment in raw_comments:
        comments[comment.id] = {'comment': comment}

        iscommented = Comment.objects.filter(iscomment=comment)
        if iscommented:
            comments[comment.id].update({'iscomment': iscommented})

    return render(
        request, 'pages/post-text.html', {
            'book': book, 'books': books, 'categories': categories, 'comments': comments})
