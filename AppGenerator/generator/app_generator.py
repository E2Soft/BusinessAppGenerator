'''
Created on Mar 16, 2015

@author: PCX
'''

from generator import specification, renderer
import os, shutil

static_files_path = os.path.join(os.path.dirname(__file__), 'static')
temp_path = os.path.join(os.path.dirname(__file__), 'temp')
temp_custom_code_path = os.path.join(temp_path, 'custom.py')

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
    project_app_name = app_model.app_name.replace(' ', '_')
    project_path = os.path.join(path, project_app_name) # root folder na osnovu imena aplikacije (razmak zamenjen sa _)
    
    copy_static_files(project_path, project_app_name)
    renderer.render(project_path, app_model, project_app_name)

def copy_static_files(project_path, project_app_name):
    '''
    Kopira strukturu direktorijuma projekta i staticke (negenerisane) fajlove.
    '''
    
    custom_code_path = os.path.join(project_path, 'business_app', 'custom.py')
    
    # remove directory if exists
    if os.path.exists(project_path):
        # save custom.py
        if os.path.exists(custom_code_path):
            shutil.move(custom_code_path, temp_custom_code_path)
        # remove old project
        shutil.rmtree(project_path)
        
    # copy static files
    shutil.copytree(static_files_path, project_path)
    
    # move saved custom.py
    if os.path.exists(temp_custom_code_path):
        shutil.move(temp_custom_code_path, custom_code_path)
    
    # rename app directory
    os.rename(os.path.join(project_path, '__app__'), os.path.join(project_path, project_app_name))
    