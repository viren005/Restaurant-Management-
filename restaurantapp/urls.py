from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.home,name='home'),
    path('menu/',views.menu,name='menu'),
    path('about/',views.about,name='about'),
    path('book/',views.booktable,name='book'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('cart/',views.cart,name='cart'),
    path('profile/',views.profile,name='profile'),
    path('addtocart/<int:id>/<str:action>/',views.addtocart,name='addtocart'),
    path('deleteitem/<int:id>/',views.deletecartItem,name='deleteitem'),
    path('categoryproduct/<int:id>/',views.categoryproduct,name='categoryproduct'),
]
