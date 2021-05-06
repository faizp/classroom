from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .models import Profile
import os
from twilio.rest import Client
from classroom import secret
import random, math


# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                if User.objects.filter(email=email).exists() or email == "":
                    messages.error(request, 'Email already exists Please provide different one')
                    return redirect('register')
                user = form.save()
                Profile.objects.create(user=user)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('profile-register')
        else:
            form = UserRegisterForm()
        return render(request, 'registration/register.html', {"form": form})
    return redirect('index')


def otp_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            phone = request.POST['phone']
            if Profile.objects.filter(phone=phone).exists():
                otp = generate_otp()
                print('hello')
                account_sid = secret.account_sid
                auth_token = secret.auth_token
                client = Client(account_sid, auth_token)

                message = client.messages \
                                .create(
                                    body="Your one time password for login in to CLASSROOM is "+otp,
                                    from_='+12512700252',
                                    to='+'+phone
                                )

                print(message)
                request.session['otp'] = otp
                request.session['phone'] = phone
                return JsonResponse('true', safe=False)
            return JsonResponse('false', safe=False)
        return render(request, 'registration/otp-login.html')
    return redirect('index')

def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def verify_otp(request):
    if not request.user.is_authenticated:
        otp_entered = request.POST['otp-entered']
        print('sdfd')
        if request.session.has_key('otp'):
            print('asd')
            otp_sent = request.session['otp']
            if otp_entered == otp_sent:
                phone = request.session['phone']
                profile = Profile.objects.get(phone=phone)
                user = User.objects.get(id=profile.user.id)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                print(phone, profile, user)
                del request.session['otp']
                del request.session['phone']
                return JsonResponse('true', safe=False)
        return JsonResponse('false', safe=False)
    return redirect('index')


def profile_register(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user = request.user)
        country = request.POST['country']
        number = request.POST['phone']
        profile.phone = country + number
        profile.status = request.POST['status']
        profile.company = request.POST['company']
        profile.bio = request.POST['bio']
        profile.image = request.POST['image']
        profile.save()
        return JsonResponse('true', safe=False)
    return render(request, 'registration/profile-register.html')