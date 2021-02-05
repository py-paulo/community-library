from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_index, name='index'),
    path('my-books', views.view_my_books, name='my-books'),
    path('access', views.view_access),
    path('post/<int:book_id>', views.view_post, name='book'),
    path('get-post', views.view_get_book, name='get-book'),
    path('category/<str:category>', views.view_books_by_category, name='filter-by-category')
]
