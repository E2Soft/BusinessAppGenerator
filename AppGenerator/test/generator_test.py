'''
Created on Mar 17, 2015

@author: PCX
'''
import unittest

from generator import generator
from test.model import AppModel, Form, Field


class Test(unittest.TestCase):

    def setUp(self):
        self.app_model = AppModel(app_name='My test app', 
                                  froms=[Form(title='First form', 
                                              fields=[Field(name='field1', label='My Field 1', field_type='String'),
                                                      Field(name='field2', label='My Field 2', field_type='String'),
                                                     ])
                                        ])

    def test_generator(self):
        generator.generate_app("test_gen", self.app_model)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()