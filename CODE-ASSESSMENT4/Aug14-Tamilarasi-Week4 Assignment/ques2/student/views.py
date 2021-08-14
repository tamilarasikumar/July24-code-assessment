from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def myStudentPage(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getAdmin_no=request.POST.get("adminno")
        getRoll_no=request.POST.get("rollno")
        getCollege=request.POST.get("college")
        getParent_name=request.POST.get("parent_name")
        dict={"name":getName,"adminno":getAdmin_no,"rollno":getRoll_no,"college":getCollege,"parent_roll":getParent_name}
        result=json.dumps(dict)
        return HttpResponse(result)
    else:
        return HttpResponse("No GET method Allowed")
   
