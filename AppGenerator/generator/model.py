'''
Created on Mar 17, 2015

@author: PCX
'''

class AppModel():
    def __init__(self, app_name=None, forms=None, packages=None):
        self.app_name=app_name
        if not forms:
            self.forms=[]
        else:
            self.forms=forms
        if not packages:
            self.packages=[]
        else:
            self.packages=packages
    
class Form:
    def __init__(self, title=None, fields=None, operations=None, main_attribute=None, 
                 display_name=None, tooltip = ""):
        self.title = title
        self.fields = fields
        self.operations = operations
        self.main_attribute = main_attribute
        self.display_name = display_name
        if not fields:
            self.fields=[]
        else:
            self.fields=fields
        if not operations:
            self.operations=[]
        else:
            self.operations=operations
        self.tooltip = tooltip 
        
class Link:
    def __init__(self, name=None,label=None, foreign_label=None, field_type=None,mandatory=False,form=None,link_type=None,weight=0):
        self.field_type = field_type
        self.mandatory = mandatory
        self.form = form
        self.label=label
        self.foreign_label=foreign_label
        self.name = name
        self.link_type = link_type
        self.weight = weight
        
class Operation:
    def __init__(self, name=None, label=None, field_type=None,param=None):
        self.name=name
        self.label=label
        self.field_type=field_type
        self.param = param

class Field:
    def __init__(self, name=None, label=None, field_type=None, mandatory = True, max_length=0, weight=0, custom_validation=False, derived=None):
        self.name=name
        self.label=label
        self.field_type=field_type #Custom->generise se samo poziv funkcije koju ce korisnik dodati, Search -> generise se search
        self.mandatory = mandatory
        self.max_length = max_length
        self.weight = weight
        self.custom_validation = custom_validation
        self.derived = derived
    
class Package:
    def __init__(self, weight=0, label = None, forms=None, subpackages=None):
        self.weight = weight
        self.label = label
        if not forms:
            self.forms=[]
        else:
            self.forms = forms
        if not subpackages:
            self.subpackages=[]
        else:
            self.subpackages = subpackages
