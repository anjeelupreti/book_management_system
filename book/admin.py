from django.contrib import admin
from book.models import (
    Publication,
    Genre,
    Book
)
# Register your models here.
admin.site.register(Publication)
admin.site.register(Genre)
admin.site.register(Book)