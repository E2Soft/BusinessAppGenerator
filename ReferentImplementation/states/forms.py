'''
Created on Mar 3, 2015

@author: Milos

'''

from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from states.models import State, City, Store

#States

class SearchStatesForm(forms.Form):
    name = forms.CharField(max_length=50,required=False)
    shortname = forms.CharField(max_length=3,required=False)
    cities = forms.MultipleChoiceField(choices=[ (o.id, str(o)) for o in City.objects.all()],
                                       required=False)
    
    def __init__(self, *args, **kwargs):
        super(SearchStatesForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'

class StatesForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ["name", "shortname", "cities"]
    
    def __init__(self, *args, **kwargs):
        super(StatesForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'

class StatesList(ListView):
    model = State
    template_name = 'states/list.html'
    context_object_name = 'states'
    
    def get_queryset(self):
        return State.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(StatesList, self).get_context_data(**kwargs)
        context["data"] = "state"
        
        return context

class StateCreate(CreateView):
    model = State
    template_name = 'states/add.html'
    form_class = StatesForm
    
    def get_success_url(self):
        return reverse('states')
    
    def get_context_data(self, **kwargs):
        context = super(StateCreate, self).get_context_data(**kwargs)
        context["data"] = "state"
        
        return context

class StateUpdate(UpdateView):
    model = State
    template_name = 'states/update.html'
    form_class = StatesForm
    
    def get_success_url(self):
        return reverse('detailstate',args=(self.get_object().id,))
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        response = super(StateUpdate, self).form_valid(form)
        
        return response
    
    def get_context_data(self, **kwargs):
        context = super(StateUpdate, self).get_context_data(**kwargs)
        context["data"] = "state"
        
        return context

class StateDetail(DetailView):
    model = State
    template_name = 'states/detail.html'
    context_object_name='object'
    
    def get_context_data(self, **kwargs):
        context = super(StateDetail, self).get_context_data(**kwargs)
        context["data"] = "state" 
        
        mapa = {}
        for name in self.object._meta.get_all_field_names():
            if "id" not in name:
                try:
                    mapa[name] = self.object.__getattribute__(name).all()
                except AttributeError:
                    try:
                        mapa[name] = self.object.__getattribute__(name)
                    except AttributeError:
                        mapa[name] = self.object.__getattribute__(''.join([name,"_set"])).all()
                        
                        
        context["mapa"] = mapa
        return context

class StateDelete(DeleteView):
    model = State
    template_name = 'states/delete.html'
    
    def get_success_url(self):
        return reverse('states')

#City

class SearchCityForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    shortname = forms.CharField(max_length=3, required=False)
    
    def __init__(self, *args, **kwargs):
        super(SearchCityForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["name", "shortname"]
    
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
        
class CityList(ListView):
    model = City
    template_name = 'states/list.html'
    context_object_name = 'states'
    
    def get_queryset(self):
        return City.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(CityList, self).get_context_data(**kwargs)
        context["data"] = "city"
        
        return context

class CityCreate(CreateView):
    model = City
    template_name = 'states/add.html'
    form_class = CityForm
    
    def get_success_url(self):
        return reverse('cities')
    
    def get_context_data(self, **kwargs):
        context = super(CityCreate, self).get_context_data(**kwargs)
        context["data"] = "city"
        
        return context

class CityUpdate(UpdateView):
    model = City
    template_name = 'states/update.html'
    form_class = CityForm
    
    def get_success_url(self):
        return reverse('deletecity',args=(self.get_object().id,))
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        response = super(CityUpdate, self).form_valid(form)
        
        return response
    
    def get_context_data(self, **kwargs):
        context = super(CityUpdate, self).get_context_data(**kwargs)
        context["data"] = "city"
        
        return context

class CityDetail(DetailView):
    model = City
    template_name = 'states/detail.html'
    context_object_name='object'
    
    def get_context_data(self, **kwargs):
        context = super(CityDetail, self).get_context_data(**kwargs)
        context["data"] = "city"
        
        mapa = {}
        for name in self.object._meta.get_all_field_names():
            if "id" not in name:
                try:
                    mapa[name] = self.object.__getattribute__(name).all()
                except AttributeError:
                    try:
                        mapa[name] = self.object.__getattribute__(name)
                    except AttributeError:
                        mapa[name] = self.object.__getattribute__(''.join([name,"_set"])).all()

        context["mapa"] = mapa
        
        return context

class CityDelete(DeleteView):
    model = City
    template_name = 'states/delete.html'
    
    def get_success_url(self):
        return reverse('states')

#Store

class SearchStoreForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    adress = forms.CharField(max_length=20, required=False)
    phone = forms.CharField(max_length=50, required=False)
    owner = forms.MultipleChoiceField(choices=[ (o.id, str(o)) for o in User.objects.all()],
                                       required=False)
    state = forms.MultipleChoiceField(choices=[ (o.id, str(o)) for o in State.objects.all()],
                                       required=False)
    city = forms.MultipleChoiceField(choices=[ (o.id, str(o)) for o in City.objects.all()],
                                       required=False)
    
    def __init__(self, *args, **kwargs):
        super(SearchStoreForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["name", "adress", "phone", "owner", "state", "city"]
    
    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        """
        self.fields["name"].widget.attrs['class']='form-control'
        self.fields["adress"].widget.attrs['class']='form-control'
        self.fields["owner"].widget.attrs['class']='form-control'
        self.fields["state"].widget.attrs['class']='form-control'
        self.fields["city"].widget.attrs['class']='form-control'
        self.fields["phone"].widget.attrs['class']='form-control'
        """
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
        
class StoreList(ListView):
    model = Store
    template_name = 'states/list.html'
    context_object_name = 'states'
    
    def get_queryset(self):
        return Store.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(StoreList, self).get_context_data(**kwargs)
        context["data"] = "store"
        
        return context

class StoreCreate(CreateView):
    model = Store
    template_name = 'states/add.html'
    form_class = StoreForm
    
    def get_success_url(self):
        return reverse('stores')
    
    def get_context_data(self, **kwargs):
        context = super(StoreCreate, self).get_context_data(**kwargs)
        context["data"] = "store"
        
        return context
    
class StoreUpdate(UpdateView):
    model = Store
    template_name = 'states/update.html'
    form_class = StoreForm
    
    def get_success_url(self):
        return reverse('detailstore',args=(self.get_object().id,))
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        response = super(StoreUpdate, self).form_valid(form)
        
        return response
    
    def get_context_data(self, **kwargs):
        context = super(StoreUpdate, self).get_context_data(**kwargs)
        context["data"] = "store"
        
        return context
    
class StoreDetail(DetailView):
    model = Store
    template_name = 'states/detail.html'
    context_object_name='object'
    
    def get_context_data(self, **kwargs):
        context = super(StoreDetail, self).get_context_data(**kwargs)
        context["data"] = "store"
        
        mapa = {}
        for name in self.object._meta.get_all_field_names():
            if 'id' not in name:
                try:
                    mapa[name] = self.object.__getattribute__(name).all()
                except AttributeError:
                    try:
                        mapa[name] = self.object.__getattribute__(name)
                    except AttributeError:
                        mapa[name] = self.object.__getattribute__(''.join([name,"_set"])).all()

        context["mapa"] = mapa
        
        return context    
    
class StoreDelete(DeleteView):
    model = Store
    template_name = 'states/delete.html'
    
    def get_success_url(self):
        return reverse('states')    


#User
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email']
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
    
class DetailUser(DetailView):
    model = User
    template_name = 'states/udetail.html'
    context_object_name='user' 
    
class UserUpdate(UpdateView):
    model = User
    template_name = 'states/uupdate.html'
    form_class = UserForm
    
    def get_success_url(self):
        return reverse('udetail',args=(self.get_object().id,))    
    
class UserCreate(CreateView):
    model = User
    template_name = 'states/register.html'
    form_class = UserForm
    
    def get_success_url(self):
        return reverse('index')    
    
    
    