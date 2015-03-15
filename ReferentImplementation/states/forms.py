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
