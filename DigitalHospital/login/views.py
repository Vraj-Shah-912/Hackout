from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
import login.models as model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
from django.http import HttpResponse
from django.views.generic import View
# from .process import html_to_pdf 
from django.template.loader import render_to_string
# Create your views here.

def loginuser(request):
       if request.user.is_authenticated:
           return redirect("pharmacy")
       
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
        # print(data)
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['userdata'] = data
            login(request,user)
            return redirect('pharmacy')
        else:
            return redirect('login.html')
              
       return render(request,'login.html')

def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('loginuser')
    else:
        return redirect('pharmacy')

def pharmacy(request):
    if request.user.is_authenticated:
        user_role=model.UserProfile.objects.all()
        username=request.session['userdata']['username']
        # username=userdata
        print(user_role)
        for i in user_role:
            # print(str(i) == str(username))
            # print(i)
            user_profile=i.role
            if str(i) == str(username):
                print('comp')
                if str(user_profile) == str('nurse'):
                    return render(request,'nurse.html')
                elif str(user_profile) == str('wardboy'):
                    return render(request,'wardboy.html')
                elif str(user_profile) == str('doctor'):
                    return render(request,'doctor.html')
                elif str(user_profile) == str('reception'):
                    return render(request,'reception.html')       
            else:
                continue
            return render(request,'pharmacy.html')
    else:
        return redirect('loginuser')