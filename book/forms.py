from django import forms
from book.models import Publication,Genre,Book



class PublicationForm(forms.ModelForm):
    class Meta:
        model=Publication
        fields='__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model=Genre
        fields='__all__'
        
        
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'