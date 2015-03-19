'''
Created on Mar 16, 2015

@author: PCX
'''

import datetime
import getpass
import os

from jinja2 import Environment, PackageLoader


env=Environment(loader=PackageLoader('generator', 'templates'))

DJANGO_APP_NAME = "business_app"

def render(project_path, app_model):
    '''
    Generise fajlove na osnovu templejta i modela aplikacije.
    '''
    render_models(project_path, app_model)
    render_views(project_path, app_model)
    render_admin(project_path, app_model)
    render_urls(project_path, app_model)
    render_forms(project_path, app_model)
    render_custom_code_file(project_path)

def render_models(project_path, app_model):
    renderedmodel = env.get_template('models').render(model = app_model,datetime=datetime.datetime.now(),
                                                      guest=getpass.getuser())
    path = project_path+"/"+DJANGO_APP_NAME
    
    with open(path+"/models.py", "w") as file:
        file.write(renderedmodel)

def render_views(project_path, app_model):
    renderedviews = env.get_template('views').render(model = app_model,datetime=datetime.datetime.now(),
                                                             guest=getpass.getuser(),app_name=DJANGO_APP_NAME)
    path = project_path+"/"+DJANGO_APP_NAME
    
    with open(path+"/views.py", "w") as file:
        file.write(renderedviews)

def render_admin(project_path, app_model):
    rendereadmin = env.get_template('admin').render(model = app_model,datetime=datetime.datetime.now(),
                                                    guest=getpass.getuser())
    path = project_path+"/"+DJANGO_APP_NAME
    
    with open(path+"/admin.py", "w") as file:
        file.write(rendereadmin)

def render_urls(project_path, app_model):
    renderedurls = env.get_template('urls').render(model = app_model,datetime=datetime.datetime.now(),
                                                     guest=getpass.getuser(),app_name=DJANGO_APP_NAME)
    path = project_path+"/"+DJANGO_APP_NAME
    
    with open(path+"/urls.py", "w") as file:
        file.write(renderedurls)

def render_forms(project_path, app_model):
    renderedforms = env.get_template('forms').render(model = app_model,datetime=datetime.datetime.now(),
                                                     guest=getpass.getuser(),app_name=DJANGO_APP_NAME)
    path = project_path+"/"+DJANGO_APP_NAME
    
    with open(path+"/forms.py", "w") as file:
        file.write(renderedforms)
        
def render_custom_code_file(project_path):
    custom_code_path = os.path.join(project_path, DJANGO_APP_NAME, 'custom.py')
    if not os.path.exists(custom_code_path):
        with open(custom_code_path, "w") as file:
            file.write("#Add custom functions here...See urls.py for more info!")
