from django import views
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.views import View
from django.core.mail import send_mail
from random import randint
from django.contrib.auth.models import User

#otp = randint(0000,9999)

# Create your views here.

def Generate_otp():
    return randint(1000,9999)

def registerView(request):
    form = UserCreationForm()
    template_name = 'AUTH_APP/registerfile.html'
    #context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage_url')
    context = {'form':form}
    return render(request, template_name, context)

def loginView(request):
    template_name = 'AUTH_APP/loginpage.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('u')
        pw = request.POST.get('p')

        global new

        user = authenticate(username = un, password = pw)
        new = user

        if user is not None:
            otp=Generate_otp()
            eml = request.POST.get('e')
            subject = "Your OTP for login to django app!"
            message = f"Hello {un}, your otp is: {otp}. Thank You!"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [eml,]
            send_mail(subject, message, email_from, recipient_list)
            response = redirect('otp_url')
            response.set_cookie('otp',otp,max_age=120)

            return response
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('loginpage_url')

def OTPview(request):
    template_name = 'AUTH_APP/otp.html'
    context={}
    if request.method == 'POST':
        otp = (request.POST.get('otp'))
        otp1 = (request.COOKIES.get('otp'))
        print(otp, otp1)

        if otp == otp1:
            login(request, new)
            return redirect('showlap_url')
    return render(request, template_name, context)