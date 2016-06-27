from django.shortcuts import render, redirect
from forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from main.models import User, UserProfile

def adduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            up = UserProfile.objects.create(user=new_user)
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            login(request, new_user)
            return redirect('../accounts/profile')
    else:
        form = UserForm()

    return render(request,
                  'registration/registration_form.html',
                  {'form': form})



def home(request):
    return render(request,'index.html')


def register(request):
    return render(request,'registration/registration_form.html')
