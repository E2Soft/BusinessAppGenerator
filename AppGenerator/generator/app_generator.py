'''
Created on Mar 16, 2015

@author: PCX
'''

from generator import specification, renderer
import os, shutil

static_files_path = os.path.join(os.path.dirname(__file__), 'static')

def generate_app_from_xml(path, xml_model_path):
    '''
    Generise aplikaciju na zadatoj lokaciji sa zadatim xml modelom aplikacije.
    '''
    app_model = specification.from_xml_file(xml_model_path)
    generate(path, app_model)
    
def generate(path, app_model):
    '''
    Generise aplikaciju na zadatoj lokaciji sa zadatim modelom aplikacije.
    '''
    app_name = app_model.app_name.replace(' ', '_')
    project_path = os.path.join(path, app_name) # root folder na osnovu imena aplikacije (razmak zamenjen sa _)
    
    copy_static_files(project_path, app_name)
    renderer.render(project_path, app_model)

def copy_static_files(project_path, app_name):
    '''
    Kopira strukturu direktorijuma projekta i staticke (negenerisane) fajlove.
    '''
    # remove directory if exists
    if os.path.exists(project_path):
        shutil.rmtree(project_path)
    # copy static files
    shutil.copytree(static_files_path, project_path)
    # rename app directory
    os.rename(os.path.join(project_path, '__app__'), os.path.join(project_path, app_name))