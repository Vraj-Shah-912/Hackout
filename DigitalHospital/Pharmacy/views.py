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

def loginuser(request):
       if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.get(email=email).username
        user_id = User.objects.get(email=email).id
        data = {
            'username':username,
            'eamil':email,
            'user_id':user_id,
        }
        request.session['userdata'] = data
        user = Authentication(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('signupuser')
        
       if request.user.is_authenticated:
           return redirect("index")
       return render(request,'loginuser.html')


