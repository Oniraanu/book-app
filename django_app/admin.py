from django.contrib import admin
from .models import Book, Publisher


admin.site.register(Publisher)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    list_display = ['title', 'price', 'isbn']
    list_editable = ['price']
    list_filter = ['publisher', 'date_published']
    search_fields = ['title']

# Register your models here.
