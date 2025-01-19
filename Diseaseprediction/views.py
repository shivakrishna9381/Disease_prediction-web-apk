
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "index.html")

def howitworks(request):
    return render(request, 'howitworks.html')

@login_required
def getstarted(request):
    return render(request, 'getstarted.html')

@login_required
def visualization(request):
    return render(request, 'visualisation.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            messages.success(request, f"Account created successfully for {username}!")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match please recheck")
    return render(request, "registrationform.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('index')

def admin_log(request):
    return redirect('admin')


def admin_logout(request):
    return redirect('index')
    
def CovidInput(request):
    return render(request, "covidinput.html")
def heartInput(request):
    return render(request, 'heartinput.html')
def diabetesInput(request):
    return render(request, "diabetesinput.html")
    
