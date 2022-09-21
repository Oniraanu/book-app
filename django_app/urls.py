from django.urls import path
from . import views

app_name = 'django_app'

urlpatterns = [
    # path("index/", views.say_hello, name='index'),
    # path("", views.redirect),
    # path("about/", views.about, name='about'),
    path('books/', views.list_of_books),
    path('book/<pk>/', views.book_detail),
    path('publishers/', views.publisher_list, name='publisher-list'),
    path('publishers/<pk>/', views.publisher_detail, name='publisher-detail')
]
