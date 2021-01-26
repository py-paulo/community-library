from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_index),
    path('my-books', views.view_my_books),
    path('access', views.view_access),
    path('post/<int:book_id>', views.view_post)
]
