from django.shortcuts import render
from book.models import Publication, genre, Book
from django.contrib.auth.models import User

def homepage(request):
    publication = Publication.objects.filter(is_active=True).count()
    Genre = genre.objects.count()
    book = Book.objects.count()
    user = User.objects.count()
    context = {
        "publication_count":publication,
        "genre_count":Genre,
        "book_count":book,
        "user_count":user,
    }
    return render(request,'home/base.html',context) 