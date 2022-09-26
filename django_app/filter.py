from django_filters import FilterSet

from django_app.models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'isbn': ['exact'],
            'title': ['exact'],
            'date_published': ['isnull', 'year__gt'],
            'price': ['gt', 'lt'],
        }
