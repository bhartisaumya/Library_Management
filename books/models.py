from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator
from django.db import models

from authors.models import Author
from genres.models import Genre


class Book(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False)
    image = models.ImageField(null=True, blank=True,)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False,)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,null=True, blank= True)

    def __str__(self):
        return self.name
