from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class PublishingCompany(models.Model):

    name = models.CharField(
        max_length=100, verbose_name='Nome')
    website = models.CharField(
        max_length=255, verbose_name='Link Website', null=True, blank=True)
    logo = models.ImageField(verbose_name='Logo', null=True, blank=True)

    def __str__(self):
        return self.name.capitalize()


class Category(models.Model):

    name = models.CharField(
        max_length=100, verbose_name='Nome')

    def __str__(self):
        return self.name.capitalize()


class Author(models.Model):

    name = models.CharField(
        max_length=255, verbose_name='Nome', blank=False, null=False, unique=True)

    def __str__(self):
        return self.name.title()


class Person(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    nickname = models.CharField(max_length=50, null=False, blank=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s" % self.nickname


class Book(models.Model):

    isbn = models.CharField(
        max_length=30, verbose_name='ISBN')
    author = models.ManyToManyField(Author, through='BookAuthor', blank=True)
    title = models.CharField(
        max_length=255, verbose_name='Titulo', blank=False, null=False, unique=False)
    subtitle = models.CharField(
        max_length=255, verbose_name='Subtitulo', blank=True, null=True, unique=True)
    display_title = models.CharField(
        max_length=50, verbose_name='Nome de exibição', blank=False, null=False)
    release_date = models.DateField(
        verbose_name='Data de lançamento', blank=True, null=True)
    category = models.ManyToManyField(Category, through='BookCategories', blank=True)
    description = models.TextField(
        verbose_name='Descrição', null=False, blank=False)
    publish_company = models.ForeignKey(PublishingCompany, on_delete=models.CASCADE, null=True, blank=True)
    display_cover = models.BooleanField(verbose_name='Exibir foto', default=False, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="Cadastrado em", blank=True, null=True)
    owner = models.ForeignKey(Person, null=True, blank=False, on_delete=models.CASCADE)

    cover = models.ImageField(verbose_name='Capa', null=True, blank=True)

    def __str__(self):
        return self.title.title()

    @property
    def display_title(self) -> str:
        title = self.title.title()
        title = title + ' ' + self.subtitle.capitalize() if self.subtitle else title
        return title

    @property
    def display_description(self):
        return self.description[:255]+'...'

    @property
    def display_categories(self):
        categories = ''
        for category in self.category.all():
            if categories == '':
                categories += category.name
            else:
                categories += ', %s' % category.name
        return categories

    @property
    def display_authors(self):
        authors = ''
        for author in self.author.all():
            if authors == '':
                authors += author.name
            else:
                authors += ', %s' % author.name
        return authors


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return '<Book %s> <Author %s>' % (self.book.title.capitalize(), self.author.name.capitalize())


class BookCategories(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return 'Book:%s, Category:%s' % (self.book.title.capitalize(), self.category.name.capitalize())


class Review(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    approved = models.BooleanField(default=False, blank=False, null=False)
    read = models.BooleanField(default=False, blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return self.title.title()


class Comment(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False)
    iscomment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=255, null=False, blank=False)
    approved = models.BooleanField(default=False, blank=False, null=False)
    read = models.BooleanField(default=False, blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return "%d - [%s] %s" % (self.id, self.author.nickname, self.book)
