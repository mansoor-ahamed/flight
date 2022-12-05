from django.contrib import admin
from django.urls import path,include
from app import views
from django.urls import path

urlpatterns = [

    path('',views.front,name='front'),
    path('',views.index,name='index'),
    path('register',views.handleRegister,name='handleRegister'),
    path('login',views.handleLogin,name='handleLogin'),
    path('logout',views.handleLogout,name='handleLogout'),
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('flight',views.handleFlight,name='handleFlight'),
    path('about',views.about,name='about'),
    path('show',views.show,name='show'),
]
