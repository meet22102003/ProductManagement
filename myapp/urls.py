from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('showproduct',views.showproductpage,name="show"),
    path('addproduct',views.addproductpage,name="add"),
    path('insertdata',views.insertproductdata,name="insert"),
    path('manageproduct',views.manageproduct,name="manage"),
    path('showproduct',views.showproductpage,name="show"),
    path('singleproduct/<int:pid>',views.singleproduct,name="singleproduct"),
    path('fetchformdata',views.fetchregdata,name="fetchformdata"),
    path('register',views.registerpage,name="register"),
    path('',views.loginpage,name="login"),
    path('fetchregdata',views.fetchregdata,name="fetchregdata"),
    path('checklogindata',views.checklogindata,name="checklogindata"),
    path('logout',views.logout,name="logout"),
    path('addtocart',views.addtocart,name="addtocart")
]