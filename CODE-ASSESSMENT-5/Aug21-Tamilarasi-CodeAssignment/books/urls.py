from django.urls import path,include
from . import views

urlpatterns = [
    path('book/',views.myBook,name='myBook'),
    path('add/',views.myBookPage,name='myBookPage'),
    path('viewall/',views.myBookList,name='myBookList'),
    path('view/<id>',views.myBookDetails,name='myBookDetails'),
    path('name/<book_name>',views.myBnameDetails,name='myBnameDetails'),
]