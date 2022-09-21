from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.urls import reverse
from .serializers import *
from rest_framework import status


# def say_hello(request):
#    context = "MUTHA "
#    return render(request, "django_app_templates/index.html", context={"name": context})


# def about(request):
#    return render(request, "django_app_templates/about.html")


# def redirect(request):
#    return HttpResponseRedirect(reverse("django_app:index"))


@api_view(['GET', 'POST'])
def list_of_books(request):
    if request.method == 'GET':
        query_set = Book.objects.all()
        serializer = BookSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail(request, pk):
    # try:
    # book = Book.objects.get(isbn=pk)
    query_set = get_object_or_404(Book, isbn=pk)
    if request.method == 'GET':
        serializer = BookSerializer(query_set, context={'request': request})
        return Response(serializer.data)
    elif request.method == ('PUT', 'PATCH'):
        serializer = BookSerializer(query_set, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        query_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # except Book.DoesNotExist:
    # return Response('error: could not find resource', status=status.HTTP_404_NOT_FOUND)


@api_view()
def publisher_list(request):
    query_set = Publisher.objects.all()
    serializer = PublisherSerializer(query_set, many=True)
    return Response(serializer.data)


@api_view()
def publisher_detail(request, pk):
    query_set = get_object_or_404(Publisher, pk=pk)
    serializer = PublisherSerializer(query_set)
    return Response(serializer.data)
