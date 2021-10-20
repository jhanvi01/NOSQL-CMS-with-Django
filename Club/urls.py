from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('deluser',views.deluser,name='deluser'),
    path('addev',views.addev,name='addev'),
    path('delev',views.delev,name='delev'),
    path('joinev',views.joinev,name='joinev'),
    path('leavev',views.leavev,name='leavev'),
    path('updatev',views.updatev,name='updatev'),
    path('contact',views.contact,name='contact'),

]
