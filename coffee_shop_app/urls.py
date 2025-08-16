from django.contrib import admin
from django.urls import path
from coffee_shop_app import views

urlpatterns = [
    path("Do_not_open/", admin.site.urls),
    path('',views.Home,name="Home"),
    path('Menu/',views.menu,name="menu"),
    path("Bill/",views.bill,name="bill"),
    path("Contact_us/",views.contact,name="contact"),
    path("login/",views.Loginuser,name="login"),
    path("logout/",views.Logoutuser,name="logout")
]
