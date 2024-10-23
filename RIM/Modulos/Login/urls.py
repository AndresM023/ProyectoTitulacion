from django.contrib import admin
from django.urls import path
from Modulos.Login.views import *

app_name = 'Login'
urlpatterns = [
    path('',Login.as_view(),name='login'),
    path('forget_password/', ForgetPassword.as_view(), name='forget_password'),
    path('change_password/',ChangePassword.as_view(),name='change_password'),
]