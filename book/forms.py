from django import forms
from book.models import Book, Publication, genre

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = genre
        fields = '__all__'
