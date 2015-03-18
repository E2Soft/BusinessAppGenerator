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
    generate_app(path, app_model)
    
def generate_app(path, app_model):
    '''
    Generise aplikaciju na zadatoj lokaciji sa zadatim modelom aplikacije.
    '''
    project_path = os.path.join(path, app_model.app_name.replace(' ', '_')) # root folder na osnovu imena aplikacije (razmak zamenjen sa _)
    copy_static_files(project_path)
    renderer.render(project_path, app_model)

def copy_static_files(project_path):
    '''
    Kopira strukturu direktorijuma projekta i staticke (negenerisane) fajlove.
    '''
    if os.path.exists(project_path):
        shutil.rmtree(project_path)
    shutil.copytree(static_files_path, project_path)