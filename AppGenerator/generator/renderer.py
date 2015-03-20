'''
Created on Mar 16, 2015

@author: PCX
'''
import datetime
import getpass

from jinja2 import Environment, PackageLoader

env=Environment(loader=PackageLoader('generator', 'project_templates'))

def render(project_path, app_model):
    '''
    Generise fajlove na osnovu templejta i modela aplikacije.
    '''
    render_models(project_path, app_model)
    render_tests(project_path, app_model)
    render_settings(project_path, app_model)
    render_wsgi(project_path, app_model)
    render_project_views(project_path, app_model)
    render_project_urls(project_path, app_model)
    
def render_models(project_path, app_model):
    #env.get_template('models.py.html').render(the='variables', go='here')
    pass

def render_tests(project_path, app_model):
    renderedtests = env.get_template('tests').render(model = app_model,datetime=datetime.datetime.now(),
                                                     guest=getpass.getuser())
    with open(project_path+"/tests.py", "w") as file:
        file.write(renderedtests)

def render_settings(project_path, app_model):
    renderedsettings = env.get_template('settings').render(model = app_model,datetime=datetime.datetime.now(),
                                                           guest=getpass.getuser(),app_name="myapp")
    with open(project_path+"/settings.py", "w") as file:
        file.write(renderedsettings)    
       
def render_project_urls(project_path, app_model):
    renderedurls = env.get_template('urls').render(model = app_model,datetime=datetime.datetime.now(),
                                                           guest=getpass.getuser(),app_name="myapp")
    with open(project_path+"/urls.py", "w") as file:
        file.write(renderedurls)

def render_project_views(project_path, app_model):
    renderedviews = env.get_template('views').render(model = app_model,datetime=datetime.datetime.now(),
                                                           guest=getpass.getuser(),app_name="myapp")
    with open(project_path+"/views.py", "w") as file:
        file.write(renderedviews)

def render_wsgi(project_path, app_model):
    renderedwsgi = env.get_template('wsgi').render(model = app_model,datetime=datetime.datetime.now(),
                                                           guest=getpass.getuser(),app_name="myapp")
    with open(project_path+"/wsgi.py", "w") as file:
        file.write(renderedwsgi)
        