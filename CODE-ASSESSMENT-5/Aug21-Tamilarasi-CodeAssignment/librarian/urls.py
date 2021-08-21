from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.myLoginLibrarian,name='myLoginLibrarian'),
    path('register/',views.myRegisterLibrarian,name='myRegisterLibrarian'),
    path('add/',views.myLibrarianPage,name='myLibrarianPage'),
    path('viewall/',views.myLibrarianList,name='myLibrarianList'),
    path('view/<id>',views.myLibrarianDetails,name='myLibrarianDetails'),
    path('code/<enroll_code>',views.myELibrarianDetails,name='myELibrarianDetails'),
]