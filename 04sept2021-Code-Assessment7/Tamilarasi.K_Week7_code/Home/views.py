from django.shortcuts import redirect,render
from Home.models import home
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Home.serializers import homeSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


# Create your views here.
def myHome(request):
    return render(request,'home.html')

def login_view(request):
    return render(request,'login.html')

def welcome_view(request):
    return render(request,'welcome.html')

@csrf_exempt
def login_view_check(request):
    try:
        username=request.POST.get("username")
        password=request.POST.get("password")
        getHome=home.objects.filter(username=username,password=password)
        Home_serializer=homeSerializer(getHome,many=True)
        print(Home_serializer.data)
        if(Home_serializer.data):
            for i in Home_serializer.data:
                x=i["name"]
                y=i["id"]
                print(x)
            request.session['uname']=x
            request.session['uid']=y
            return render(request,"home.html")
        else:
            return HttpResponse("Invalid Credentials")
    except home.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")