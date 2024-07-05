from django.db import models
from author.models import Author

# Create your models here.
class Publication(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()
    website = models.URLField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    


class Genre(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='book/',blank=True, null=True)
    image = models.ImageField(upload_to='book/images',null=True,blank=True)
    publication = models.ForeignKey(Publication, on_delete=models.RESTRICT)
    genre = models.ManyToManyField(Genre)
    author = models.ManyToManyField(Author)
    edition = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    ISBN_number = models.CharField(null=True, blank=True,max_length=40)
    page_number = models.IntegerField()
    description = models.CharField(max_length=255, null=True,blank=True)
    demo_text = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=9, decimal_places=2)
    volume = models.IntegerField()
    language = models.CharField(max_length=10, null=True, blank=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name