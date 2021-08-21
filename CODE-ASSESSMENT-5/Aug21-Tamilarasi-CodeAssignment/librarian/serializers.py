from rest_framework import fields, serializers
from librarian.models import Librarian
class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Librarian
        fields=('enroll_code','name','address','mblno','username','password')