'''
Created on Mar 19, 2015

@author: PCX
'''
import os, sys

from django.core.management import call_command


class Manager():
    def __init__(self, project_path, app_name):
        # add app to PYTHON_PATH
        sys.path.append(project_path)
        
        os.environ['DJANGO_SETTINGS_MODULE'] = app_name+'.settings'
        
        # setup django
        import django
        django.setup()

    def migrate_database(self):
        # create database
        call_command('makemigrations')
        call_command('migrate')

    def create_super_user(self, username, password, email=None):
        from django.contrib.auth.models import User
        if User.objects.filter(username=username):
            print('user '+username+' already exists')
        else:
            User.objects.create_superuser(username=username, password=password, email=email if email else 'test@test.com')
    
    def run_server(self):
        # create database
        call_command('runserver')