from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
    

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email']
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'

class UserCreate(CreateView):
    model = User
    template_name = 'states/register.html'
    form_class = RegistrationForm
    
    def get_success_url(self):
        return reverse('home')