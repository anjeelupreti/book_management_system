from django.urls import path
# from .views import list_books,delete_book,edit_book,
from .views import list_publication, create_publication, update_publication,delete_publication
from .views import list_genre,create_genre,update_genre,delete_genre

 



urlpatterns = [
    # path('list/',list_books,name='list_books'),
    # path('delete/<id>',delete_book,name='delete_book'),
    # path('edit/<id>',edit_book,name='edit_book'),
        path("publication/list",list_publication ,name='list_publication'),
    path("publication/create",create_publication,name='create_publication'),
    path("publication/update/<id>",update_publication,name='update_publication'),
    path('publication/delete/<id>/', delete_publication, name='delete_publication'),
    path('genre/list/',list_genre,name='list_genre'),
    path('genre/create/',create_genre,name='create_genre'),
    path('genre/update/<id>',update_genre,name='update_genre'),
    path('genre/delete/<id>',delete_genre,name='delete_genre'),
    
    
    
    
]