from rest_framework import serializers
from django_app.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'email', 'url']


class BookSerializer(serializers.ModelSerializer):
    publisher = serializers.HyperlinkedRelatedField(
        queryset=Publisher.objects.all(),
        view_name='django_app:publisher-detail'
    )

    class Meta:
        model = Book
        fields = '__all__'
