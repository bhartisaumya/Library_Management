from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from books.models import Book
from books.serializers import BookSerializer
from utils.paginator import StandardPaginator


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = StandardPaginator
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'name', 'price', 'author__name']
    search_fields = ['author__name', 'genre__name', 'name']
    ordering_fields = ['id', 'price']
