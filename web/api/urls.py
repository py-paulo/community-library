from library.models import Book, BookAuthor, BookCategories

from django.urls import path, include

from rest_framework import routers, serializers, viewsets
from rest_framework import permissions


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'isbn', 'author', 'title', 'subtitle', 'display_title', 'release_date', 
            'category', 'description', 'publish_company', 'display_cover', 'created_at',
            'owner', 'rented', 'cover'
        ]


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = [
            'book', 'author'
        ]


class BookCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategories
        fields = [
            'book',
            'category'
        ]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAdminUser]


class BookCategoriesViewSet(viewsets.ModelViewSet):
    queryset = BookCategories.objects.all()
    serializer_class = BookCategoriesSerializer

    permission_classes = [permissions.IsAdminUser]


class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer

    permission_classes = [permissions.IsAdminUser]


router = routers.DefaultRouter()

router.register(r'book', BookViewSet)
router.register(r'book-author', BookAuthorViewSet)
router.register(r'book-category', BookCategoriesViewSet)

urlpatterns = [
    path('', include(router.urls))
]