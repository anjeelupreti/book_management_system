from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import Book, Genre, Publication
from .forms import BookForm, GenreForm, PublicationForm

@login_required
def list_publication(request):
    publications = Publication.objects.filter(is_active=True)
    context = {
        "publications": publications
    }
    return render(request, 'publication/index.html', context)

@login_required
def create_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publication added successfully.')  
            return redirect('list_publication') 
        else:
            messages.error(request, 'Error adding publication. Please check the form.')  
    else:
        form = PublicationForm()

    context = {'form': form}
    return render(request, 'publication/create.html', context)

@login_required
def update_publication(request, id):
    publication = get_object_or_404(Publication, id=id)
    form = PublicationForm(request.POST or None, instance=publication)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_publication')
        else:
            print(form.errors)
    
    context = {'form': form}
    return render(request, 'publication/update.html', context)

@login_required
def delete_publication(request, id):
    publication = get_object_or_404(Publication, id=id)
    publication.delete()
    return redirect('list_publication')

@login_required
def list_genre(request):
    genres = Genre.objects.all()
    active_genres = Genre.objects.filter(is_active=True)
    context = {
        'genres': genres,
        'active_genres': active_genres
    }
    return render(request, 'genre/index.html', context)

@login_required
def create_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_genre')
        else:
            print(form.errors)
    else:
        form = GenreForm()

    context = {"form": form}
    return render(request, "genre/create.html", context)

@login_required
def update_genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    form = GenreForm(request.POST or None, instance=genre)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_genre')
        else:
            print(form.errors)

    context = {
        "genre": genre,
        "form": form
    }
    return render(request, 'genre/update.html', context)

@login_required
def delete_genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    genre.delete()
    return redirect('list_genre')

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = BookForm()
    
    context = {'form': form}
    return render(request, 'book/create.html', context)

def read_book(request, id):
    book = get_object_or_404(Book, id=id)
    context = {
        'book': book  
    }
    return render(request, 'book/read.html', context)


def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    
    form = BookForm(instance=book)

    context = {
        'form': form,
        'book': book  
    }
    return render(request, 'book/update.html', context)

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_book')

def list_book(request):
    books = Book.objects.filter(is_active=True).order_by('-name')
    context = {'books': books}
    return render(request, 'book/index.html', context)
