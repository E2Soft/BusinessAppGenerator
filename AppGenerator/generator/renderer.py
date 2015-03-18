'''
Created on Mar 16, 2015

@author: PCX
'''

import datetime
import getpass

from jinja2 import Environment, PackageLoader


env=Environment(loader=PackageLoader('generator', 'templates'))

def render(project_path, app_model):
    '''
    Generise fajlove na osnovu templejta i modela aplikacije.
    '''
    render_models(project_path, app_model)
    render_views(project_path, app_model)
    render_admin(project_path, app_model)
    render_urls(project_path, app_model)
    render_forms(project_path, app_model)
    print("JOB DONE")

def render_models(project_path, app_model):
    renderedmodel = env.get_template('models').render(model = app_model,datetime=datetime.datetime.now(),
                                                      guest=getpass.getuser())
    with open(project_path+"/models.py", "w") as file:
        file.write(renderedmodel)

def render_views(project_path, app_model):
    #env.get_template('views.py.html').render(the='variables', go='here')
    pass

def render_admin(project_path, app_model):
    #env.get_template('models.py.html').render(the='variables', go='here')
    pass

def render_urls(project_path, app_model):
    #env.get_template('models.py.html').render(the='variables', go='here')
    pass

def render_forms(project_path, app_model):
    #env.get_template('models.py.html').render(the='variables', go='here')
    pass