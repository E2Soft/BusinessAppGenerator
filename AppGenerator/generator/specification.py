'''
Created on Mar 13, 2015

@author: zeljko.bal
'''

from lxml import objectify

from generator.model import AppModel, Form, Field, Operation, Link


def from_xml_file(file_path):
    with open(file_path, 'r') as fileobject:
        xml_model = objectify.parse(fileobject).getroot()
        return _create_app_model(xml_model)
    
def from_xml_string(xml):
    xml_model = objectify.fromstring(xml)
    return _create_app_model(xml_model)

def _create_app_model(xml_model):
    app_model = AppModel()
    app_model.app_name = xml_model.app_name.text
    
    for xml_form in xml_model.forms.Form:
        app_model.forms.append(_create_form_model(xml_form))

    return app_model

def _create_form_model(xml_form):
    form = Form()
    form.title = xml_form.title.text
    form.display_name = xml_form.display_name.text
    form.main_attribute = xml_form.main_attribute.text
    
    if hasattr(xml_form.fields, 'Field'):
        for xml_field in xml_form.fields.Field:
            field = Field()
            if hasattr(xml_field, 'max_length'):
                field.max_length = int(xml_field.max_length.text)
            field.name = xml_field.name.text
            field.label = xml_field.label.text
            field.field_type = xml_field.field_type.text
            field.mandatory = xml_field.mandatory.text.lower() == 'true'
            field.weight = int(xml_field.weight.text)
            
            form.fields.append(field)
       
    if hasattr(xml_form.fields, 'Link'):
        for xml_field in xml_form.fields.Link:
            field = Link()
            field.form = xml_field.form.text
            field.foreign_label = xml_field.foreign_label.text
            field.link_type = xml_field.link_type.text
            
            field.name = xml_field.name.text
            field.label = xml_field.label.text
            field.field_type = xml_field.field_type.text
            field.mandatory = xml_field.mandatory.text.lower() == 'true'
            field.weight = int(xml_field.weight.text)
            
            form.fields.append(field)
    
    if hasattr(xml_form.operations, 'Operation'):
        for xml_operation in xml_form.operations.Operation:
            operation = Operation()
            operation.name = xml_operation.name.text
            operation.label = xml_operation.label.text
            operation.field_type = xml_operation.field_type.text
            operation.param = xml_operation.param.text.lower() == 'true'
            
            form.operations.append(operation)
    
    return form
