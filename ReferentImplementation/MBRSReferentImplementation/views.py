'''
Created on Mar 3, 2015

@author: Milos
'''
from django.shortcuts import render


def home(request):
    return render(request,'states/main.html')