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

def render(project_path, app_model, project_app_name):
    '''
    Generise fajlove na osnovu templejta i modela aplikacije.
    '''
    render_models(project_path, app_model)
    render_views(project_path, app_model)
    render_admin(project_path, app_model)
    render_urls(project_path, app_model)
    render_forms(project_path, app_model)
    render_custom(project_path, app_model)
    render_manage(project_path, app_model, project_app_name)
    render_tests(project_path, app_model)
    render_settings(project_path, app_model, project_app_name)
    render_wsgi(project_path, app_model, project_app_name)
    render_project_views(project_path, app_model, project_app_name)
    render_project_urls(project_path, app_model, project_app_name)
    render_templatetags(project_path, app_model)
    render_custom_validators(project_path, app_model)
    render_derived_fields(project_path, app_model)

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
        
def render_manage(project_path, app_model, project_app_name):
    renderedmanage = env.get_template('manage').render(name = project_app_name,
                                                       datetime=datetime.datetime.now(),guest=getpass.getuser())
    with open(project_path+"/manage.py", "w") as file:
        file.write(renderedmanage)
        
def render_custom(project_path, app_model):
    custom_code_path = os.path.join(project_path, DJANGO_APP_NAME, 'custom.py')
    if not os.path.exists(custom_code_path):
        renderedcustom = env.get_template('custom').render(model = app_model,datetime=datetime.datetime.now(), guest=getpass.getuser())
        with open(custom_code_path, "w") as file:
            file.write(renderedcustom)

def render_tests(project_path, app_model):
    renderedtests = env.get_template('tests').render(model = app_model,datetime=datetime.datetime.now(),
                                                     guest=getpass.getuser())
    
    path = project_path+"/"+DJANGO_APP_NAME

    with open(path+'/tests.py', "w") as file:
        file.write(renderedtests)

def render_settings(project_path, app_model, project_app_name):
    renderedsettings = env.get_template('settings').render(model = app_model,datetime=datetime.datetime.now(),
                                                           guest=getpass.getuser(),app_name=project_app_name)
    with open(os.path.join(project_path, project_app_name, 'settings.py'), "w") as file:
        file.write(renderedsettings)    
       
def render_project_urls(project_path, app_model, project_app_name):
    renderedurls = env.get_template('project_urls').render(model = app_model,datetime=datetime.datetime.now(),
                                                           guest=getpass.getuser(),app_name=project_app_name)
    with open(os.path.join(project_path, project_app_name, 'urls.py'), "w") as file:
        file.write(renderedurls)

def render_project_views(project_path, app_model, project_app_name):
    renderedviews = env.get_template('project_views').render(model = app_model,datetime=datetime.datetime.now(),
                                                           guest=getpass.getuser(),app_name=project_app_name)
    with open(os.path.join(project_path, project_app_name, 'views.py'), "w") as file:
        file.write(renderedviews)

def render_wsgi(project_path, app_model, project_app_name):
    renderedwsgi = env.get_template('wsgi').render(model = app_model,datetime=datetime.datetime.now(),
                                                           guest=getpass.getuser(),app_name=project_app_name)
    with open(os.path.join(project_path, project_app_name, 'wsgi.py'), "w") as file:
        file.write(renderedwsgi)

def render_templatetags(project_path, app_model):
    renderedtemplatetags = env.get_template('templatetags').render(model = app_model,datetime=datetime.datetime.now(),
                                                                   guest=getpass.getuser(),app_name=DJANGO_APP_NAME)
    path = project_path+"/"+DJANGO_APP_NAME
    
    with open(path+"/templatetags/business_app_extras.py", "w") as file:
        file.write(renderedtemplatetags)

def render_custom_validators(project_path, app_model):
    custom_code_path = os.path.join(project_path, DJANGO_APP_NAME, 'custom_validators.py')
    if not os.path.exists(custom_code_path):
        rendered_data = env.get_template('custom_validators').render(model = app_model,datetime=datetime.datetime.now(),
                                                                   guest=getpass.getuser(),app_name=DJANGO_APP_NAME)
    
        with open(custom_code_path, 'w') as file:
            file.write(rendered_data)

def render_derived_fields(project_path, app_model):
    custom_code_path = os.path.join(project_path, DJANGO_APP_NAME, 'derived_fields.py')
    if not os.path.exists(custom_code_path):
        rendered_data = env.get_template('derived_fields').render(model = app_model,datetime=datetime.datetime.now(),
                                                                   guest=getpass.getuser(),app_name=DJANGO_APP_NAME)
    
        with open(custom_code_path, 'w') as file:
            file.write(rendered_data)
    
