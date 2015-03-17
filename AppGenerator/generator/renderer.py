'''
Created on Mar 16, 2015

@author: PCX
'''

from jinja2 import Environment, PackageLoader

env=Environment(loader=PackageLoader('generator', 'templates'))

def render(project_path, app_model):
    '''
    Generise fajlove na osnovu templejta i modela aplikacije.
    '''
    render_models(project_path, app_model)
    render_views(project_path, app_model)

def render_models(project_path, app_model):
    #env.get_template('models.py.html').render(the='variables', go='here')
    pass

def render_views(project_path, app_model):
    #env.get_template('views.py.html').render(the='variables', go='here')
    pass