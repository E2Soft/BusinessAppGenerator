'''
Created on Mar 3, 2015

@author: Milos
'''
from django.conf.urls import patterns, url

from states import views
from states.forms import StatesList, CityList, StoreList, StateCreate, \
    CityCreate, StoreCreate, StateUpdate, CityUpdate, StoreUpdate, StateDetail,\
    CityDetail, StoreDetail, StateDelete, CityDelete, StoreDelete
    
from states.forms import DetailUser,UserUpdate,UserCreate

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    url(r'^states/$', StatesList.as_view(), name='states'),
    
    url(r'^addstate/$', StateCreate.as_view(), name='addstate'),
    url(r'^updatestate/(?P<pk>\d+)/$', StateUpdate.as_view(), name='updatestate'),
    url(r'^detailestate/(?P<pk>\d+)/$', StateDetail.as_view(), name='detailstate'),
    url(r'^deletestate/(?P<pk>\d+)/$', StateDelete.as_view(), name='deletestate'),
    url(r'^searchstate/$', views.searchstate, name='searchstate'),
    
    url(r'^cities/$', CityList.as_view(), name='cities'),
    url(r'^addcity/$', CityCreate.as_view(), name='addcity'),
    url(r'^updatecity/(?P<pk>\d+)/$', CityUpdate.as_view(), name='updatecity'),
    url(r'^detailcity/(?P<pk>\d+)/$', CityDetail.as_view(), name='detailcity'),
    url(r'^deletecity/(?P<pk>\d+)/$', CityDelete.as_view(), name='deletecity'),
    url(r'^searchcity/$', views.searchcity, name='searchcity'),
    
    url(r'^stores/$', StoreList.as_view(), name='stores'),
    url(r'^addstore/$', StoreCreate.as_view(), name='addstore'),
    url(r'^updatestore/(?P<pk>\d+)/$', StoreUpdate.as_view(), name='updatestore'),
    url(r'^detailstore/(?P<pk>\d+)/$', StoreDetail.as_view(), name='detailstore'),
    url(r'^deletestore/(?P<pk>\d+)/$', StoreDelete.as_view(), name='deletestore'),
    url(r'^searchstore/$', views.searchstore, name='searchstore'),
    
    url(r'^udetail/(?P<pk>\d+)/$', DetailUser.as_view(), name='udetail'),
    url(r'uedit/(?P<pk>\d+)/$', UserUpdate.as_view(), name='uedit'),
    url(r'register/', UserCreate.as_view(), name='register'),
    
)
