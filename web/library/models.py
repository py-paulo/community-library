from datetime import datetime
from django.db import models


class PublishingCompany(models.Model):

    name = models.CharField(
        max_length=100, verbose_name='Nome')
    website = models.CharField(
        max_length=255, verbose_name='Link Website')
    logo = models.ImageField(verbose_name='Logo')


class Category(models.Model):

    name = models.CharField(
        max_length=100, verbose_name='Nome')


class Author(models.Model):

    name = models.CharField(
        max_length=255, verbose_name='Nome', blank=False, null=False, unique=True)
    birthday = models.DateField(
        verbose_name='Data de nascimento')


class Book(models.Model):

    isbn = models.CharField(
        max_length=30, verbose_name='ISBN')
    author = models.ManyToManyField(Author)
    title = models.CharField(
        max_length=255, verbose_name='Titulo', blank=False, null=False, unique=False)
    subtitle = models.CharField(
        max_length=255, verbose_name='Subtitulo', blank=True, null=True, unique=True)
    display_title = models.CharField(
        max_length=50, verbose_name='Nome de exibição', blank=False, null=False)
    release_date = models.DateField(
        verbose_name='Data de lançamento', blank=True, null=True)
    category = models.ManyToManyField(Category)
    description = models.TextField(
        verbose_name='Descrição', null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="Cadastrado em", blank=True, null=True)

    cover = models.ImageField(verbose_name='Capa', null=True, blank=True)

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
