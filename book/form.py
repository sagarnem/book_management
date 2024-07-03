from django import forms
from book.models import Book, Publication, genre

class createbookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class createpublicationform(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'

class creategenreform(forms.ModelForm):
    class Meta:
        model = genre
        fields = '__all__'

