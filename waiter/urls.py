from django.urls import path
from . import views

urlpatterns = [   
        path('waiterlogin/',views.waiterlogin,name='waiterlogin'),
        path('waiterlogout/',views.waiterlogout,name='waiterlogout'),
        path('waiterdashboard/',views.waiterdashboard,name='waiterdashboard'),
        path('waitermenu/<int:tableno>/<category>',views.waitermenu,name='waitermenu'),
        path('waitercart/<int:tableno>/<int:productid>/<action>',views.waitercart,name='waitercart'),
        path('proceed/<int:tableno>/',views.proceed,name='proceed'),
        path('completeorder/<int:tableno>/',views.complateorder,name='completeorder'),
        path('changepassword/',views.changepasswordwaiter,name='changepasswordwaiter'),
]