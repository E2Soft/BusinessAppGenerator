

from django.contrib import auth
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render

from states.forms import  SearchStatesForm, SearchCityForm, \
    SearchStoreForm
from states.models import State, City, Store


# Create your views here.
def index(request):
    if request.user.is_authenticated():
        context = {"isadmin":request.user.is_superuser,"user":request.user}
        return render(request,'states/main.html',context)
     
    username = request.POST.get("username","")
    password = request.POST.get("password","")
    
    user = auth.authenticate(username=username, password=password)
    context = {"isadmin":request.user.is_superuser,"user":request.user}
    
    if user is not None:
        auth.login(request, user)
        contextt = {"isadmin":request.user.is_superuser,"user":user}
        return render(request,'states/main.html',contextt) 
     
    else:
        return render(request,'states/login.html')

def searchstate(request):
    
    if request.method == 'POST':
        form = SearchStatesForm(request.POST)

        if form.is_valid():
            objects = State.objects.filter(Q(name__icontains=form.cleaned_data['name'])|
                                           Q(shortname__icontains=form.cleaned_data['shortname'])|
                                           Q(cities__in=form.cleaned_data['cities']))
            
            result = {}
            for val in objects.all():
                result[reverse('detailstate',args=(val.id,))]=val.name
            
            return render(request, 'states/result.html', {"results":result})
        
    else:
        form = SearchStatesForm()
        
    return render(request, 'states/search.html', {'form': form,'data':"State"})

def searchcity(request):
    
    if request.method == 'POST':
        form = SearchCityForm(request.POST)

        if form.is_valid():
            objects = City.objects.filter(Q(name__icontains=form.cleaned_data['name'])|
                                           Q(shortname__icontains=form.cleaned_data['shortname']))
            
            result = {}
            for val in objects.all():
                result[reverse('detailcity',args=(val.id,))]=val.name
            
            return render(request, 'states/result.html', {"results":result})
        
    else:
        form = SearchCityForm()
        
    return render(request, 'states/search.html', {'form': form,'data':"City"})

def searchstore(request):
    
    if request.method == 'POST':
        form = SearchStoreForm(request.POST)
        
        if form.is_valid():
            objects = Store.objects.filter(Q(name__icontains=form.cleaned_data['name'])|
                                          Q(adress__icontains=form.cleaned_data['adress'])|
                                          Q(phone__icontains=form.cleaned_data['phone'])|
                                          Q(state__in=form.cleaned_data['state'])|
                                          Q(city__in=form.cleaned_data['city'])|
                                          Q(owner__in=form.cleaned_data['owner']))
            
            result = {}
            for val in objects.all():
                result[reverse('detailstore',args=(val.id,))]=val.name
            
            return render(request, 'states/result.html', {"results":result})
        
    else:
        form = SearchStoreForm()
        
    return render(request, 'states/search.html', {'form': form,'data':"Store"})
