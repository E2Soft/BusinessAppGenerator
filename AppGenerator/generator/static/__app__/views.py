
from django.shortcuts import render
from django.contrib import auth

def home(request):
    if request.user.is_authenticated():
        context = {"isadmin":request.user.is_superuser,"user":request.user}
        return render(request,'business_app/main.html',context)
     
    username = request.POST.get("username","")
    password = request.POST.get("password","")
    
    user = auth.authenticate(username=username, password=password)
    context = {"isadmin":request.user.is_superuser,"user":request.user}
    
    if user is not None:
        auth.login(request, user)
        contextt = {"isadmin":request.user.is_superuser,"user":user}
        return render(request,'business_app/main.html',contextt) 
     
    else:
        return render(request,'business_app/login.html')
    
def logout(request):
    auth.logout(request)
    return render(request, 'business_app/login.html')