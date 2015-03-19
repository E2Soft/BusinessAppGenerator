'''
Created on Mar 17, 2015

@author: PCX
'''

class AppModel():
    def __init__(self, app_name=None, forms=[]):
        self.app_name=app_name
        self.forms=forms
    
class Form:
    def __init__(self, title=None, fields=[], operations=[], main_attribute=None):
        self.title = title
        self.fields = fields
        self.operations = operations
        self.main_attribute = main_attribute

class Link:
    def __init__(self, name=None,label=None, field_type=None,mandatory=False,form=None,link_type=None):
        self.field_type = field_type
        self.mandatory = mandatory
        self.form = form
        self.label=label
        self.name = name
        self.link_type = link_type

class Operation:
    def __init__(self, name=None, label=None, field_type=None,param=None):
        self.name=name
        self.label=label
        self.field_type=field_type
        self.param = param

class Field:
    def __init__(self, name=None, label=None, field_type=None, mandatory = True, max_length=0):
        self.name=name
        self.label=label
        self.field_type=field_type #Custom->generise se samo poziv funkcije koju ce korisnik dodati, Search -> generise se search
        self.mandatory = mandatory
        self.max_length = max_length