import logging

from jsonschema import validate

from django.shortcuts import render, redirect

from library.models import Book, Category, Comment, Person, Review, BookCategories
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage

logger = logging.getLogger(__name__)

GET_BOOK_SCHEMA = {
    "type" : "object",
    "properties" : {
        "book" : {"type" : "string"}
    },
}


def view_access(request):
    return render(request, 'auth/access.html')


@login_required()
def view_get_book(request):
    try:
        validate(instance=request.POST, schema=GET_BOOK_SCHEMA)
    except ValidationError as err:
        pass

    attrs = request.POST
    my_user = Person.objects.get(user=request.user)

    try:
        book = Book.objects.get(id=int(attrs.get('book')))
    except ValueError as err:
        pass
    else:
        if book.owner == my_user:
            pass # TODO não é possível alugar porque você é o dono do livro.

    return redirect('book', book_id=request.POST.get('book'))


@login_required()
def view_index(request):
    book_list = Book.objects.all()[::-1]
    paginator = Paginator(book_list, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        books = paginator.page(page)
    except (EmptyPage, InvalidPage):
        books = paginator.page(paginator.num_pages)

    return render(
        request, 'pages/index.html', {'books': books})


def view_books_by_category(request, category):
    book_category_list = BookCategories.objects.filter(category__name=category)[::-1]

    book_list = [book_category.book for book_category in book_category_list]
    paginator = Paginator(book_list, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        books = paginator.page(page)
    except (EmptyPage, InvalidPage):
        books = paginator.page(paginator.num_pages)

    return render(
        request, 'pages/index.html', {'books': books})


@login_required()
def view_my_books(request):
    book_list = Book.objects.filter(owner=Person.objects.get(user=request.user))

    paginator = Paginator(book_list, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        books = paginator.page(page)
    except (EmptyPage, InvalidPage):
        books = paginator.page(paginator.num_pages)

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
        raw_comments = Comment.objects.filter(approved=True).filter(author=book.owner).filter(book=book)

    for comment in raw_comments:
        comments[comment.id] = {'comment': comment}

        iscommented = Comment.objects.filter(iscomment=comment)
        if iscommented:
            comments[comment.id].update({'iscomment': iscommented})

    html = 'post-text.html' if not book.display_cover else 'img-post-text.html'

    reviews = Review.objects.filter(book=book)

    return render(
        request, 'pages/%s' % html, {
            'book': book, 'books': books, 'categories': categories, 'comments': comments, 'reviews': reviews
        })
