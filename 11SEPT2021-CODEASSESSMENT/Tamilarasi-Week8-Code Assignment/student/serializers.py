from rest_framework import fields, serializers
from student.models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('id','name','address','sclass','mobile','username','password')