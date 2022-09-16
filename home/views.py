from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    dict={
        'tut':Tutorial.objects.all
        }
    return render(request,'index.html',dict)


def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'New Accound has Created: {username}')
            return redirect('home:login')
        else:
            print(form.errors)
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Logging in Successfully: {username}')
                return redirect('home:index')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')

    form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_request(request):
    logout(request,)
    messages.success(request, 'Logged out successfully')
    return redirect('/')