'''
Created on Apr 2, 2015

@author: PCX
'''
from test import test_data
import unittest

from generator import specification


class Test(unittest.TestCase):

    def setUp(self):
        self.app_model = specification.from_xml_string(test_data.test_app_string)

    def testSpecificationParsing(self):
        self.assertEqual(self.app_model.app_name, 'StorageApp')
        
        self.assertEqual(len(self.app_model.forms), 8)
        
        user_form = self.app_model.forms[0]
        self.assertEqual(user_form.title, 'User')
        self.assertEqual(user_form.display_name, 'User')
        self.assertEqual(user_form.main_attribute, 'ime')
        self.assertEqual(user_form.tooltip, 'Allow viewing and manipulation of all Users')
        
        self.assertEqual(len(user_form.fields), 4)
        self._test_field(field_model=user_form.fields[0],
                         name='ime',
                         label='Name',
                         field_type='String',
                         mandatory=False,
                         weight=1,
                         max_length=20)
        
        self.assertEqual(len(user_form.operations), 1)
        self._test_operation(operation_model=user_form.operations[0], 
                             name='Search', 
                             label='Search', 
                             field_type='Search', 
                             param=False)
        
        item_form = self.app_model.forms[5]
        self.assertEqual(item_form.title, 'Item')
        self.assertEqual(item_form.display_name, 'Item')
        self.assertEqual(item_form.main_attribute, 'nazivArtikal')
        self.assertEqual(item_form.tooltip, 'Allow viewing and manipulation of all Articles')
        
        self._test_field(field_model=item_form.fields[1],
                 name='kolicina',
                 label='Quantity',
                 field_type='Integer',
                 mandatory=True,
                 weight=2,
                 max_length=100)
        self._test_field(field_model=item_form.fields[2],
                 name='pojedinacnaCena',
                 label='Single item price',
                 field_type='Float',
                 mandatory=True,
                 weight=3,
                 max_length=100)
        self._test_link(link_model=item_form.fields[4], 
                        name='relationship3',
                        label='Declaration',
                        field_type='Link',
                        mandatory=True,
                        weight=1,
                        form='Declaration', 
                        link_type='1-*', 
                        foreign_label='Item')
        self._test_operation(operation_model=item_form.operations[0], 
                     name='Search', 
                     label='Search', 
                     field_type='Search', 
                     param=False)
        self._test_operation(operation_model=item_form.operations[1], 
                     name='Popust', 
                     label='Discount', 
                     field_type='Custom', 
                     param=False)
        
        self._test_package(package_model=self.app_model.packages[0], 
                           name='Items', 
                           label='Items', 
                           weight=1, 
                           forms=[self.app_model.forms[5], 
                                  self.app_model.forms[6], 
                                  self.app_model.forms[3],
                                  self.app_model.forms[2],
                                  self.app_model.forms[1],
                                  ]
                           )
        
        self._test_package(self.app_model.packages[1], 
                           name='User', 
                           label='User', 
                           weight=2, 
                           forms=[self.app_model.forms[0], 
                                  self.app_model.forms[7], 
                                  self.app_model.forms[4],
                                  ]
                           )
    
    def _test_field(self, field_model, name, label, field_type, mandatory, weight, max_length=None):
        self.assertEqual(field_model.name, name)
        self.assertEqual(field_model.label, label)
        self.assertEqual(field_model.field_type, field_type)
        self.assertEqual(field_model.mandatory, mandatory)
        self.assertEqual(field_model.weight, weight)
        self.assertEqual(field_model.max_length, max_length)
        
    def _test_operation(self, operation_model, name, label, field_type, param):
        self.assertEqual(operation_model.name, name)
        self.assertEqual(operation_model.label, label)
        self.assertEqual(operation_model.field_type, field_type)
        self.assertEqual(operation_model.param, param)
        
    def _test_link(self, link_model, name, label, field_type, mandatory, weight, form, link_type, foreign_label):
        self.assertEqual(link_model.name, name)
        self.assertEqual(link_model.label, label)
        self.assertEqual(link_model.field_type, field_type)
        self.assertEqual(link_model.mandatory, mandatory)
        self.assertEqual(link_model.weight, weight)
        self.assertEqual(link_model.form, form)
        self.assertEqual(link_model.link_type, link_type)
        self.assertEqual(link_model.foreign_label, foreign_label)
    
    def _test_package(self, package_model, name, label, weight, forms):
        self.assertEqual(package_model.name, name)
        self.assertEqual(package_model.label, label)
        self.assertEqual(package_model.weight, weight)
        form_titles = [f.title for f in package_model.forms]
        self.assertEqual(len(form_titles), len(forms))
        for form in forms:
            self.assertIn(form.title, form_titles)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()