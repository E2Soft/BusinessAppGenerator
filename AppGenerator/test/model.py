'''
Created on Mar 17, 2015

@author: PCX
'''

class AppModel():
    def __init__(self, app_name=None, forms=[]):
        self.app_name=app_name
        self.forms=forms
    
class Form:
    def __init__(self, title=None, fields=[]):
        self.title=title
        self.fields=fields

class Field:
    def __init__(self, name=None, label=None, field_type=None):
        self.name=name
        self.label=label
        self.field_type=field_type