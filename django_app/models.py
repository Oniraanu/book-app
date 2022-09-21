from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=255, verbose_name="Publisher Name")
    email = models.EmailField(unique=True)
    url = models.URLField()


class Book(models.Model):
    GENRE_CHOICES = (
        ('COMEDY', 'Comedy'),
        ('ROMANCE', 'Romance'),
        ('FICTION', 'Fiction'),
        ('DRAMA', 'Drama')
    )
    title = models.CharField(max_length=255, verbose_name="Book Title")
    description = models.TextField(default="Any Text")
    date_published = models.DateField(auto_now=True)
    isbn = models.CharField(max_length=20, primary_key=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    books = models.ManyToManyField(Book, related_name='Authors', through='BookAuthor')


class BookAuthor(models.Model):
    ROLES = (
        ('AUTHOR', 'Author'),
        ('CO-AUTHOR', 'Co-Author'),
        ('EDITOR', 'Editor')
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    roles = models.CharField(max_length=255, choices=ROLES)


class Address(models.Model):
    number = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, default='Lagos')
    country = models.CharField(max_length=255, default='Nigeria')
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE, primary_key=True)
