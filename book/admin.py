from django.contrib import admin
from book.models import Publication, Book, genre

# Register your models here.

admin.site.register(Publication)
admin.site.register(genre)
admin.site.register(Book)