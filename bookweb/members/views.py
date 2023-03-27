from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webofbooks:homepage')
        else:
            messages.success(request, "Podczas próby zalogowania się pojawił się problem. Spróbuj jeszcze raz.")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Zostałeś wylogowany!")
    return redirect('webofbooks:homepage')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Gratulacje! Rejestracja powiodła się. Jesteś użytkownikiem Web of Books.")
            return redirect('webofbooks:homepage')
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register_user.html', {'form':form,})