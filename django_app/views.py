from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_app.filter import BookFilter
from django_app.models import Book, Publisher
from django_app.serializers import BookSerializer, PublisherSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'isbn']
    ordering_fields = ['title', 'price']
    ordering = ['asc']


class BookDetailsViewSet(ModelViewSet):
    queryset = Book.objects.get_queryset()
    serializer_class = BookSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetailsViewSet(ModelViewSet):
    queryset = Publisher.objects.get_queryset()
    serializer_class = PublisherSerializer
