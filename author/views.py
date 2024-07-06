from django.shortcuts import render, redirect,get_object_or_404
from author.models import Author
from author.forms import AuthorForm
from django.contrib import messages 
from django.http import HttpResponse

# Create your views here.


def list_author(request):
    authors = Author.objects.filter(is_active=True)
    context = {"authors": authors}
    return render(request, "author/index.html", context)



def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author added successfully.')
            return redirect('list_author')
        else:
            # If form is invalid, handle the errors
            messages.error(request, 'Form submission error. Please check the form.')
            print(form.errors)  # Print errors to console for debugging
    else:
        form = AuthorForm()

    context = {'form': form}
    return render(request, 'author/create.html', context)

def read_author(request, id):
    author = get_object_or_404(Author, id=id)
    context = {
        'author': author  
    }
    return render(request, 'author/read.html', context)

def update_author(request, id):
    data = Author.objects.get(id=id)
    form = AuthorForm(instance=data)
    if request.method == "POST":
        form = AuthorForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect("list_author")
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "author/update.html", context)


def delete_author(request, id):
    Author.objects.get(id=id).delete()
    return redirect("list_author")
