from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Login(TemplateView):
    template_name = 'login.html'


class ForgetPassword(TemplateView):
    template_name = 'forget_password.html'

class ChangePassword(TemplateView):
    template_name = 'change_password.html'

