'''
Created on Mar 13, 2015

@author: zeljko.bal
'''

from lxml import objectify

from generator.model import AppModel, Form, Field, Operation, Link, Package


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
    all_forms_map = {}
    
    for xml_form in xml_model.forms.Form:
        form_model = _create_form_model(xml_form)
        app_model.forms.append(form_model)
        all_forms_map[form_model.title] = form_model

    app_model.packages += _create_sub_packages(xml_model, all_forms_map)

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
            if hasattr(xml_field, 'custom_validation'):
                field.custom_validation = xml_field.custom_validation.text.lower() == 'true'
            if hasattr(xml_field, 'derived'):
                field.derived = xml_field.derived.text
            
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

def _create_sub_packages(xml_package, all_forms_map):
    sub_packages=[]
    if hasattr(xml_package.packages, 'Package'):
        for sub_package in xml_package.packages.Package:
            sub_packages.append(_create_package_model(sub_package, all_forms_map))
    return sub_packages

def _create_package_model(xml_package, all_forms_map):
    package = Package()
    package.name = xml_package.name.text
    package.label = xml_package.label.text
    package.weight = int(xml_package.weight.text)
    
    for form in xml_package.forms.Form:
        form_title = form.xpath(form.get('reference'))[0].title
        package.forms.append(all_forms_map[form_title])
    
    package.packages += _create_sub_packages(xml_package, all_forms_map)
    
    return package

