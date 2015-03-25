'''
Created on Mar 3, 2015

@author: Milos
'''
from django import template
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from states.models import Store, City, State
from builtins import str


register = template.Library()

@register.filter
def classname(obj):
    return obj.__class__.__name__ != "QuerySet"

@register.filter
def filternormal(obj):
    filtered = [ (key,value) for key,value in obj.items() if value.__class__.__name__ != "QuerySet"]
    return filtered

@register.filter
def filterlists(obj):
    filtered = [ (key,value) for key,value in obj.items() if value.__class__.__name__ == "QuerySet"]
    return filtered

@register.filter
def filterurl(obj):
    if isinstance(obj, Store):
        return reverse('detailstore',args=(obj.id,))
    elif isinstance(obj, City):
        return reverse('detailcity',args=(obj.id,))
    elif isinstance(obj, State):
        return reverse('detailstate',args=(obj.id,))
    else:
        return reverse('udetail',args=(obj.id,))
    
@register.filter
def isstring(obj):
    return isinstance(obj, str) #or isinstance(obj, User)