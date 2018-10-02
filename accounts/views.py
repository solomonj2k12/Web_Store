from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import userloginform


def index(request):
    '''Return the index.html file '''
    return render(request, 'index.html')
    
def logout(request):
    ''' log the user out '''
    auth.logout(request)
    messages.success(request, "You Have Successfully Logged Out!")
    return redirect(reverse('index'))
    
def login(request):
    
    
    if request.method == "POST":
        login_form = userloginform(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
                                     
            messages.success(request, "You Have Successfully Logged Into Your Account")
            
            if user:
                auth.login(user=user, request=request)
            else:
                login_form.add_error(None, "Your Username Or Password Is Invalid")
    else:
        login_form = userloginform()
    return render(request, 'login.html', {'login_form': login_form})