from django.shortcuts import render
from book.models import Publication, Genre, Book
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    publication_count = Publication.objects.filter(is_active=True).count()
    genre_count = Genre.objects.count()
    book_count = Book.objects.count()
    user_count = User.objects.count()
    context = {
        "publication_count":publication_count,
        "genre_count":genre_count,
        "book_count":book_count,
        "user_count":user_count,
    }
    return render(request,'home/base.html',context) 