'''
Created on Mar 3, 2015

@author: Milos
'''
from django.conf.urls import patterns, url
from states import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
)