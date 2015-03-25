'''
Created on Mar 16, 2015

@author: PCX
'''

from generator import specification, renderer
import os, shutil

static_files_path = os.path.join(os.path.dirname(__file__), 'static')
temp_dir_path = os.path.join(os.path.dirname(__file__), 'temp')

def generate_app_from_xml(path, xml_model_path=None, xml_model_string=None, **kwargs):
    '''
    Generise aplikaciju na zadatoj lokaciji sa zadatim xml modelom aplikacije.
    '''
    if (xml_model_path and xml_model_string) or not(xml_model_path or xml_model_string):
        raise Exception('Provide either xml_model_path or xml_model_string.')
    if xml_model_path:
        app_model = specification.from_xml_file(xml_model_path)
    if xml_model_string:
        app_model = specification.from_xml_string(xml_model_string)
    generate(path, app_model, **kwargs)
    
    return app_model
    
def generate(path, app_model, **kwargs):
    '''
    Generise aplikaciju na zadatoj lokaciji sa zadatim modelom aplikacije.
    '''
    project_app_name = app_model.app_name.replace(' ', '_')
    project_path = os.path.join(path, project_app_name) # root folder na osnovu imena aplikacije (razmak zamenjen sa _)
    
    copy_static_files(project_path, project_app_name, **kwargs)
    renderer.render(project_path, app_model, project_app_name)

def copy_static_files(project_path, project_app_name, **kwargs):
    '''
    Kopira strukturu direktorijuma projekta i staticke (negenerisane) fajlove.
    '''
    rewrite_db = kwargs.get('rewrite_db')
    rewrite_migrations = kwargs.get('rewrite_migrations')
    
    app_path = os.path.join(project_path, 'business_app')
    
    # remove directory if exists
    if os.path.exists(project_path):
        backup(app_path, 'custom.py')
        if not rewrite_db:
            backup(project_path, 'db.sqlite3')
        if not rewrite_migrations:
            backup(app_path, 'migrations')
        # remove old project
        shutil.rmtree(project_path)
        
    # copy static files
    shutil.copytree(static_files_path, project_path)
    
    # move saved custom.py
    restore(app_path, 'custom.py')
    restore(project_path, 'db.sqlite3')
    restore(app_path, 'migrations')
    
    # rename app directory
    os.rename(os.path.join(project_path, '__app__'), os.path.join(project_path, project_app_name))

def backup(dir_path, name):
    temp_path = os.path.join(temp_dir_path, name)
    target_path = os.path.join(dir_path, name)
    if os.path.exists(target_path):
        shutil.move(target_path, temp_path)

def restore(dir_path, name):
    temp_path = os.path.join(temp_dir_path, name)
    target_path = os.path.join(dir_path, name)
    if os.path.exists(temp_path):
        shutil.move(temp_path, target_path)
    