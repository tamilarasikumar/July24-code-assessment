from rest_framework import fields, serializers
from books.models import Books
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=('book_name','author','description','publisher','price')