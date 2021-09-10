from django.urls import path,include
from . import views

urlpatterns = [
    path('student/',views.myStudent,name='myStudent'),
    path('welcome/',views.myWelcome,name='myWelcome'),
    path('viewallstudent1/',views.myViewAllPage1,name='myViewAllPage1'),
    path('searchstudent/',views.mySearch1 ,name='mySearch1'),
    path('update1/',views.myUpdate1,name='myUpdate1'),
    path('delete1/',views.myDelete1,name='myDelete1'),
  
    path('deletesearch1/',views.DeleteSearchAPI1,name='DeleteSearchAPI1'),
    path('deleteread1/',views.DeleteRead1,name='DeleteRead1'),
    path('updateread1/',views.UpdateRead1,name='UpdateRead1'),
    path('updatesearch1/',views.UpdateSearchAPI1,name='UpdateSearchAPI1'),
    path('add/',views.myStudentPage,name='myStudentPage'),
    path('viewall/',views.myStudentList,name='myStudentList'),
    path('view/<id>',views.myStudentDetails,name='myStudentDetails'),
    path('search1/',views.SearchAPI1,name='SearchAPI1'),

    path('signin_check/',views.signin_check,name='signin_check'),
    path('signin/',views.signin,name='signin'),
    path('wel/',views.wel,name='wel'),
    
    
]