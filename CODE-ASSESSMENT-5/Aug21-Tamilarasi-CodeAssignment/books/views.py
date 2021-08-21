from django.shortcuts import render
from books.models import Books
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from books.serializers import BooksSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def myBook(request):
    return render(request,'book.html')

@csrf_exempt
def myBookDetails(request,id):
    try:
        book=Books.objects.get(id=id)
        if (request.method=="GET"):    
            books_serializer=BooksSerializer(book)
            return JsonResponse(books_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            book.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            books_serialize=BooksSerializer(book,data=dict)
            if(books_serialize.is_valid()):
                books_serialize.save()
                return JsonResponse(books_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(books_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Books.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

def myBnameDetails(request,book_name):
    book=Books.objects.get(book_name=book_name)
    if (request.method=="GET"):    
        books_serializer=BooksSerializer(book)
        return JsonResponse(books_serializer.data,safe=False,status=status.HTTP_200_OK)


@csrf_exempt
def myBookList(request):
    if(request.method=="GET"):
        book=Books.objects.all()
        books_serializer=BooksSerializer(book,many=True)
        return JsonResponse(books_serializer.data,safe=False)

@csrf_exempt
def myBookPage(request):
    if(request.method=="POST"):
        dict=JSONParser().parse(request)
        books_serialize=BooksSerializer(data=dict)
        if(books_serialize.is_valid()):
            books_serialize.save()
            return JsonResponse(books_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
        