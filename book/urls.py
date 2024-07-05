from django.urls import path
from book.views import (
    list_publication,
    create_publication,
    edit_publication,
    list_genre,
    create_genre,
    edit_genre,
    delete_genre,
    delete_publication,
    create_book,
    list_book,
    edit_book,
    delete_book
)

urlpatterns = [
    path("publication/list", list_publication, name="list_publication"),
    path("publication/create", create_publication, name="create_publication"),
    path("publication/edit/<id>", edit_publication, name="edit_publication"),
    path("publication/delete/<id>/", delete_publication, name="delete_publication"),
    path("genre", list_genre, name="list-genre"),
    path("create_genre", create_genre, name="create-genre"),
    path("edit_genre/<id>", edit_genre, name="edit-genre"),
    path("delete_genre/<id>", delete_genre, name="delete-genre"),
    path("book", list_book, name="list-book"),
    path("create_book", create_book, name="create-book"),
    path("edit_book/<id>", edit_book, name="edit-book"),
    path("delete_book/<id>", delete_book, name="delete-book"),
]
