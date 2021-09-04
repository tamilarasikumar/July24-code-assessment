from django.urls import path, include
from . import views

urlpatterns = [

    path('home/',views.myHome,name='myHome'),
    path('loginview/',views.login_view,name='login_view'),

    path('login/', views.login_view_check, name='login_view_check'),
   
]