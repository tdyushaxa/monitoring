from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


def LoginPageView(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('main:update')
    return render(request,'login.html',{'form':form})


def LogoutPageView(request):
    logout(request)
    return redirect('main:computer')