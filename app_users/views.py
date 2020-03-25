from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group, User

from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='member')
            user.groups.add(group)

            messages.success(request, 'An account was created for ' + username )
            return redirect('login')

    context = {'form' : form }
    return render(request, 'app_users/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try: 
            user = authenticate(request, username=User.objects.get(email=username), password=password)
        except:
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is Incorrect')

    return render(request, 'app_users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')