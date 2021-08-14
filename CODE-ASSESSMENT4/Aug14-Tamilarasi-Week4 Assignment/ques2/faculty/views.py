from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def myFacultyPage(request):
    if(request.method=="POST"):
        getName=request.POST.get("faculty_name")
        getAddress=request.POST.get("address")
        getDepartment=request.POST.get("department")
        getCollege=request.POST.get("college")
        dict={"faculty_name":getName,"address":getAddress,"department":getDepartment,"college":getCollege}
        result=json.dumps(dict)
        return HttpResponse(result)
    else:
        return HttpResponse("No GET method Allowed")