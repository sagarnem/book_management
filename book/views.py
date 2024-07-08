from django.shortcuts import render, redirect
from book.models import Publication, genre, Book
from book.forms import PublicationForm, GenreForm, Bookform
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def list_publication(request):
    publication = Publication.objects.all()
    context = {"publication": publication}
    return render(request, "publication/index.html", context)

@login_required()
def create_publication(request):
    form = PublicationForm()
    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/book/publication/list")
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "publication/create.html", context)

@login_required()
def edit_publication(request, id):
    data = Publication.objects.get(id=id)
    form = PublicationForm(instance=data)
    if request.method == "POST":
        form = PublicationForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("/book/publication/list")
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "publication/edit.html", context)


@login_required()
def delete_publication(request, id):
    Publication.objects.get(id=id).delete()
    return redirect('/book/publication/list')

@login_required()
def list_genre(request):
    Genre = genre.objects.filter(is_active=True)
    context = {'genre':Genre}
    return render(request, 'genre/index.html', context)

@login_required()
def create_genre(request):
    form = GenreForm()
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book/genre')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request, 'genre/create.html', context)

@login_required()
def edit_genre(request,id):
    data = genre.objects.get(id=id)
    form = GenreForm(instance=data)
    if request.method == 'POST':
        form = GenreForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/book/genre')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request, 'genre/edit.html', context)

@login_required()
def delete_genre(request,id):
    Genre = genre.objects.get(id=id).delete()
    return redirect('/book/genre')

@login_required()
def list_genre(request):
    Genre = genre.objects.all()
    context = {'genre':Genre}
    return render(request, 'genre/index.html', context)

@login_required()
def list_book(request):
    book = Book.objects.filter(is_active=True)
    context = {'book':book}
    return render(request, 'book/index.html', context)

@login_required()
def create_book(request):
    form = Bookform()
    if request.method == 'POST':
        form = Bookform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/book/book')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request, 'book/create.html', context)

@login_required()
def edit_book(request,id):
    data = Book.objects.get(id=id)
    form = Bookform(instance=data)
    if request.method == 'POST':
        form = Bookform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/book/book')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request, 'book/edit.html', context)

@login_required()
def delete_book(request,id):
    book = Book.objects.get(id=id).delete()
    return redirect('/book/book')

@login_required()
def view_profile(request,id):
    reader = Book.objects.get(id=id)
    

    context={
        'data':reader
    }
    return render(request,'book/view.html',context)
