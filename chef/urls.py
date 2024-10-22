from django.urls import path
from . import views

urlpatterns = [   
        path('cheflogin/',views.cheflogin,name='cheflogin'),
        path('cheflogout/',views.cheflogout,name='cheflogout'),
        path('neworder/',views.neworder,name='neworder'),
        path('complete/<int:id>',views.complete,name='complete'),
        path('completeorder/',views.completeorder,name='completeorder'),
        path('changepasswordchef/',views.changepassword,name='changepasswordchef'),

]