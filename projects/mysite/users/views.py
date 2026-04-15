from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegistrationUser
# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegistrationUser(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}')
            return redirect('login')
    form=RegistrationUser()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')