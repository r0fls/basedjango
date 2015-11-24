from django.shortcuts import render
from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

def adduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            return HttpResponseRedirect('main.html')
    else:
        form = UserForm() 

    return render(request, 'adduser.html', {'form': form}) 
