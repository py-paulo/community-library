from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_index),
    path('access', views.view_access),
    path('login', views.view_login),
    path('post/<int:book_id>', views.view_post)
]
