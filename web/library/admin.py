from django.contrib import admin
from .models import Category, PublishingCompany, Author, Book, BookAuthor, BookCategories, Review, Person, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(PublishingCompany)
class PublishingCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(BookCategories)
class BookCategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
