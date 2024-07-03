from django.urls import path
from book.views import create_book, Book_view, create_genre, create_publication

urlpatterns = [
    path("create-book", create_book ,name="create_book"),
    path('', Book_view.as_view(), name="list"),
    path("create-publication", create_publication ,name="create_publication"),
    path("create-genre", create_genre ,name="create_genre")

]