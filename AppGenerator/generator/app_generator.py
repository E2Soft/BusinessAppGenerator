'''
Created on Mar 16, 2015

@author: PCX
'''
from generator import specification, renderer

def generate_from_xml(project_path, xml_model_path):
    '''
    Generise aplikaciju na zadatoj lokaciji sa zadatim xml modelom aplikacije.
    '''
    app_model = specification.from_xml_file(xml_model_path)
    generate(project_path, app_model)
    
def generate(project_path, app_model):
    copy_static_files(project_path)
    renderer.render(project_path, app_model)

def copy_static_files(project_path):
    '''
    Kopira strukturu direktorijuma projekta i staticke (negenerisane) fajlove.
    '''
    pass