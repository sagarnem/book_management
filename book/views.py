from django.shortcuts import render, redirect
from book.form import createbookform, createpublicationform, creategenreform
from django.views.generic import ListView
from book.models import Book


# Create your views here.

def create_book(request):
    form = createbookform
    if request.method == 'POST':
        form =  createbookform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)

    context={
        "form": form
    }

    return render(request, 'book/create.html', context)

def create_publication(request):
    form = createpublicationform
    if request.method == 'POST':
        form =  createpublicationform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)

    context={
        "form": form
    }

    return render(request, 'book/index.html', context)


def create_genre(request):
    form = creategenreform
    if request.method == 'POST':
        form =  creategenreform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)

    context={
        "form": form
    }

    return render(request, 'book/index.html', context)


class Book_view(ListView):
    model=Book
    template_name = 'book/index.html'
    context_oject_data = 'data'



