'''
Created on Mar 13, 2015

@author: zeljko.bal
'''

from lxml import objectify

def from_xml_file(file_path):
    with open(file_path, 'r') as fileobject:
        app_model = objectify.parse(fileobject).getroot()
        return _process_model(app_model)
    
def from_xml_string(xml):
    app_model = objectify.fromstring(xml)
    return _process_model(app_model)

def _process_model(app_model):
    
    _resolve_links(app_model)
    
    app_model.forms = [_process_form(f) for f in app_model.forms.Form]
    
    return app_model

def _process_form(form):
    if hasattr(form.fields, 'FormField'):
        form_fields = [f for f in form.fields.FormField]
    else:
        form_fields = []
    if hasattr(form.fields, 'LinkField'):
        link_fields = [f for f in form.fields.LinkField]
    else:
        link_fields = []
    
    form.fields = form_fields + link_fields
    
    if hasattr(form.operations, 'Operation'):
        form.operations = [o for o in form.operations.Operation]
    else:
        form.operations = []
    
    return form

def _resolve_links(app_model):
    for form in app_model.forms.Form:
        if hasattr(form.fields, 'LinkField'):
            for link in form.fields.LinkField:
                link.form = link.form.xpath(link.form.get('reference'))[0]

