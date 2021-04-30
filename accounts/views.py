from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

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
                form.save()
                return redirect('index')
        else:
            form = UserRegisterForm()
        return render(request, 'registration/register.html', {"form": form})
    return redirect('index')