from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.views import APIView

from .serializers import *
from rest_framework import status


class BookList(APIView):
    def get(self, request):
        query_set = Book.objects.all()
        serializer = BookSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class BookDetail(APIView):
    def get(self, request, pk):
        query_set = get_object_or_404(Book, isbn=pk)
        serializer = BookSerializer(query_set, context={'request': request})
        return Response(serializer.data)

    def patch(self, request, pk):
        query_set = get_object_or_404(Book, isbn=pk)
        serializer = BookSerializer(query_set, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query_set = get_object_or_404(Book, isbn=pk)
        query_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublisherList(APIView):
    def get(self, request):
        query_set = Book.objects.all()
        serializer = PublisherSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class PublisherDetail(APIView):
    def get(self, request, pk):
        query_set = get_object_or_404(Book, pk=pk)
        serializer = PublisherSerializer(query_set, context={'request': request})
        return Response(serializer.data)

    def patch(self, request, pk):
        query_set = get_object_or_404(Book, pk=pk)
        serializer = PublisherSerializer(query_set, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query_set = get_object_or_404(Book, pk=pk)
        query_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
