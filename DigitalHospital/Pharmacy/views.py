from django.shortcuts import render
from httplib2 import Authentication
from django.shortcuts import render,HttpResponse,redirect
import Pharmacy.models as model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
from django.http import HttpResponse
from django.views.generic import View
# from .process import html_to_pdf 
from django.template.loader import render_to_string


# Create your views here.
def login(request):
    print("heloo")
    return render(request,'login.html')


