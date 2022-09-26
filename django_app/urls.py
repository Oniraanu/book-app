from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

app_name = 'django_app'

router = DefaultRouter()
router.register('books', views.BookViewSet)
router.register('publishers', views.PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("index/", views.say_hello, name='index'),
    # path("", views.redirect),
    # path("about/", views.about, name='about'),
    # path('books/', views.BookList.as_view()),
    # path('books/<pk>/', views.BookDetail.as_view()),
    # path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    # path('publishers/<pk>/', views.PublisherDetail.as_view(), name='publisher-detail')
]
