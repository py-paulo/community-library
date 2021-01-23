from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_index),
    path('post/<int:id>', views.view_post)
]
