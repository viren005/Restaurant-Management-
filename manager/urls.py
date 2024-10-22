from django.urls import path
from . import views

urlpatterns = [   
        path('managerlogin/',views.managerlogin,name='managerlogin'),
        path('managerlogout/',views.managerlogout,name='managerlogout'),
        path('managerdashboard/',views.managerdashboard,name='managerdashboard'),
        path('addwaiter/',views.addwaiter,name='addwaiter'),
        path('addchef/',views.addchef,name='addchef'),
        path('listofchef/',views.listofchef,name='listofchef'),
        path('listofwaiter/',views.listofwaiter,name='listofwaiter'),
        path('addtable/',views.addtable,name='addtable'),
        path('listoftable/',views.listoftable,name='listoftable'),
        path('deletechef/<int:id>',views.deletechef,name='deletechef'),
        path('deletewaiter/<int:id>',views.deletewaiter,name='deletewaiter'),
        path('deletetable/<int:id>',views.deletetable,name='deletetable'),
        path('changepassword/',views.changepassword,name='changepassword'),
]