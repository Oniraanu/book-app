from django.urls import path
from . import views

app_name = 'django_app'

urlpatterns = [
    # path("index/", views.say_hello, name='index'),
    # path("", views.redirect),
    # path("about/", views.about, name='about'),
    path('books/', views.BookList.as_view()),
    path('book/<pk>/', views.BookDetail.as_view()),
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publishers/<pk>/', views.PublisherDetail.as_view(), name='publisher-detail')
]
