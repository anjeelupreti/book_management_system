from .models import Book,Genre,Publication
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.http import HttpResponse
# from .form import EditBookForm,
from .form import GenreForm
from book.models import Publication
from book.form import PublicationForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def list_publication(request):
    publication = Publication.objects.filter(is_active=True)
    context = {
        "publication":publication
    }
    return render(request,'publication/index.html',context)

@login_required

def create_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publication added successfully.')  # Add success message
            return redirect('list_publication')  # Redirect to the list view
        else:
            messages.error(request, 'Error adding publication. Please check the form.')  # Add error message
    else:
        form = PublicationForm()

    context = {'form': form}
    return render(request, 'publication/create.html', context)


@login_required
def update_publication(request,id):
    publication = Publication.objects.get(id=id)
    form = PublicationForm(instance=publication)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/book/publication/list')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request,'publication/edit.html',context)

@login_required
def delete_publication(request,id):
    Publication.objects.get(id=id).delete()
    return redirect('/book/publication/list')

@login_required
def list_genre(request):
    genres=Genre.objects.all()
    active_genres=Genre.objects.filter(is_active=True)
    context={
        'genres':genres,
        'active_genres':genres
    }
    return render(request,'genre/index.html',context)

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
def update_genre(request,id):
    genre = Genre.objects.get(id=id)
    form = GenreForm(instance=genre)
    if request.method=='POST':
        form =GenreForm(request.POST , instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre/index.html')
        else:
            print(form.errors)
    context ={
        "data":genre,
        "form":form
    }
    return render(request,'genre/edit.html',context)

@login_required
def delete_genre(request, id):
    Genre.objects.get(id=id).delete()
    return redirect('genre/index.html')



    
    



# Create your views here.

# def delete_book(request,id):
    
#     book =Book.objects.get(id=id)
#     book.delete()
#     return redirect('list_books')
       
    
    
# def list_books(request):
#     context={
#         'books':Book.objects.all().order_by('-name')
        
#     }
#     # return render(request,'file',context)
    
# def edit_book(request,id):
#     book=Book.objects.get(id=id)
#     if request.method=='POST':
#         form = BookForm(request.POST, request.FILES, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('list/')
#     else:
#         form = BookForm(instance=book) 
#         return render(request, 'file', {'form': form})
    
    

    
