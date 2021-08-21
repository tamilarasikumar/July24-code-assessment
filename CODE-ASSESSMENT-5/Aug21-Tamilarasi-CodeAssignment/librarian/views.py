from django.shortcuts import render
from librarian.models import Librarian
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from librarian.serializers import LibrarianSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def myLoginLibrarian(request):
    return render(request,'login.html')

def myRegisterLibrarian(request):
    return render(request,'register.html')

@csrf_exempt
def myLibrarianDetails(request,id):
    try:
        librarians=Librarian.objects.get(id=id)
        if (request.method=="GET"):    
            librarian_serializer=LibrarianSerializer(librarians)
            return JsonResponse(librarian_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            librarians.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            librarian_serialize=LibrarianSerializer(librarians,data=dict)
            if(librarian_serialize.is_valid()):
                librarian_serialize.save()
                return JsonResponse(librarian_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(librarian_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

def myELibrarianDetails(request,enroll_code):
    librarians=Librarian.objects.get(enroll_code=enroll_code)
    if (request.method=="GET"):    
        librarian_serializer=LibrarianSerializer(librarians)
        return JsonResponse(librarian_serializer.data,safe=False,status=status.HTTP_200_OK)


@csrf_exempt
def myLibrarianList(request):
    if(request.method=="GET"):
        librarians=Librarian.objects.all()
        librarian_serializer=LibrarianSerializer(librarians,many=True)
        return JsonResponse(librarian_serializer.data,safe=False)

@csrf_exempt
def myLibrarianPage(request):
    if(request.method=="POST"):
        dict=JSONParser().parse(request)
        librarian_serialize=LibrarianSerializer(data=dict)
        if(librarian_serialize.is_valid()):
            librarian_serialize.save()
            return JsonResponse(librarian_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
        