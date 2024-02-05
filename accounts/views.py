from django.shortcuts               import render, redirect
from django.contrib.auth            import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib                 import messages
from django.views.decorators.csrf   import csrf_exempt


from .forms                         import *


def join_us(request):
    signup = CreateuserForm
    if request.method == 'POST':
        signup = CreateuserForm(request.POST)
        if signup.is_valid():
            signup.save()
            user = signup.cleaned_data.get('username')
            messages.success(request,'Accounts was created for ' + str(user))
            
            #login 
            username = request.POST.get('username')
            password = request.POST.get('password1')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home:home')

    if request.user.is_authenticated:
        return redirect('home:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home:home')
            else:
                messages.info(request, 'username or password is incorrect')
    context = {
        'signup':signup,
        # 'signin':signin,
    }
    
    return render(request, 'sign in & sign up.html', context)

def logout_user(request):
    logout(request)
    return redirect('home:home')

