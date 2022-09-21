from rest_framework.viewsets import ModelViewSet

from django_app.models import Book, Publisher
from django_app.serializers import BookSerializer, PublisherSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailsViewSet(ModelViewSet):
    queryset = Book.objects.get_queryset()
    serializer_class = BookSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetailsViewSet(ModelViewSet):
    queryset = Publisher.objects.get_queryset()
    serializer_class = PublisherSerializer
