import student
from django.shortcuts import render,redirect
from student.models import Student
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from student.serializers import StudentSerializer
from rest_framework.parsers import JSONParser
import requests

# Create your views here.

@csrf_exempt
def myStudent(request):
    return render(request,'student.html')

def myWelcome(request):
    return render(request,'welcome1.html')


def myViewAllPage1(request):
    fetchdata=requests.get("http://127.0.0.1:8000/student/viewall/").json()
    return render(request,'viewall1.html',{"data":fetchdata})

def mySearch1(request):
    return render(request,'search1.html')

def myUpdate1(request):
    return render(request,'update1.html')


def myDelete1(request):
    return render(request,'delete1.html')


@csrf_exempt
def myStudentDetails(request,id):
    try:
        students=Student.objects.get(id=id)
        if(request.method=="GET"):
            student_serializer=StudentSerializer(students)
            return JsonResponse(student_serializer.data,safe=False)
        if(request.method=="DELETE"):
            students.delete()
            return HttpResponse("Deleted")
        if(request.method=="PUT"):
            dict=JSONParser().parse(request)
            student_serialize=StudentSerializer(data=dict)
            if(student_serialize.is_valid()):
                student_serialize.save()
                return JsonResponse(student_serialize.data)
            else:
                return JsonResponse(student_serialize.errors)
    except Student.DoesNotExist:
        return HttpResponse("Invalid")



@csrf_exempt
def myStudentPage(request):
    if(request.method=="POST"):
        # dict=JSONParser().parse(request)
        student_serialize=StudentSerializer(data=request.POST)
        if(student_serialize.is_valid()):
            student_serialize.save()
            return redirect(myUpdate1)
            # return JsonResponse(student_serialize.data)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("Get method is not allowed")

@csrf_exempt
def myStudentList(request):
    if(request.method=="GET"):
        students=Student.objects.all()
        student_serializer=StudentSerializer(students,many=True)
        return JsonResponse(student_serializer.data,safe=False)

@csrf_exempt
def UpdateRead1(request):
    getNewId=request.POST.get("newid")
    getNewname=request.POST.get("newname")
    getNewaddress=request.POST.get("newaddress")
    getNewclass=request.POST.get("newclass")
    getNewmobile=request.POST.get("newmobile")
    getNewusername=request.POST.get("newusername")
    getNewpassword=request.POST.get("newpassword")
    
    mydata={'name':getNewname,'address':getNewaddress,'sclass':getNewclass,'mobile':getNewmobile,'username':getNewusername,'password':getNewpassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/student/view/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return redirect(myViewAllPage1)
    

@csrf_exempt
def UpdateSearchAPI1(request):
    try:
        getName=request.POST.get("name")
        getAddress=Student.objects.filter(name=getName)
        student_serializer=StudentSerializer(getAddress,many=True)
        return render(request,"update1.html",{"data":student_serializer.data})
        #return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")


# Create your views here.
@csrf_exempt
def DeleteRead1(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/student/view/" + getNewId
    requests.delete(ApiLink)
    return redirect(myViewAllPage1)

@csrf_exempt
def DeleteSearchAPI1(request):
    try:
        getName=request.POST.get("name")
        getAddress=Student.objects.filter(name=getName)
        student_serializer=StudentSerializer(getAddress,many=True)
        return render(request,"delete1.html",{"data":student_serializer.data})
        #return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

@csrf_exempt
def SearchAPI1(request):
    try:
        getName=request.POST.get("name")
        getAddress=Student.objects.filter(name=getName)
        student_serializer=StudentSerializer(getAddress,many=True)
        return render(request,"search1.html",{"data":student_serializer.data})
        #return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")


def signin(request):
    return render(request,'signin.html')

def wel(request):
    return render(request,'wel.html')


@csrf_exempt
def signin_check(request):
    try:
        username=request.POST.get("username")
        password=request.POST.get("password")
        getstudent=Student.objects.filter(username=username,password=password)
        student_serializer=StudentSerializer(getstudent,many=True)
        print(student_serializer.data)
        if(student_serializer.data):
            for i in student_serializer.data:
                x=i["id"]
                y=i["name"]
                z=i["address"]
                a=i["sclass"]
                b=i["mobile"]
                # print(x)
            request.session['uid']=x
            request.session['uname']=y
            request.session['uaddress']=z
            request.session['uclass']=a
            request.session['umobile']=b
            return render(request,"update1.html")
        else:
            return HttpResponse("Invalid Credentials")
    except Student.DoesNotExist:
        return HttpResponse("Invalid name",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
