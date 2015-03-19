'''
Created on Mar 19, 2015

@author: PCX
'''
import os
from test import test_data

from generator import app_generator
from generator.manage import Manager


if __name__ == "__main__":
    app_model = test_data.test_app_model
    app_name=app_model.app_name.replace(' ', '_')
    project_path = os.path.join('test_gen', app_name)
    
    manager = Manager(project_path, app_name)
    
    app_generator.generate("test_gen", app_model)
    manager.migrate_database()
    manager.create_super_user(username='asd', password='asd')
    manager.run_server()