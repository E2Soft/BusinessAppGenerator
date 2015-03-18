'''
Created on Mar 17, 2015

@author: PCX
'''
import unittest

from generator import generator
from test.model import AppModel, Form, Field, Link


class Test(unittest.TestCase):

    def setUp(self):
        self.app_model = AppModel(app_name='My test app', 
                                  forms=[Form(title='Firstform', 
                                              fields=[Field(name='field1', label='My Field 1', field_type='String',
                                                            mandatory=True,max_length=4),
                                                      Field(name='field2', label='My Field 2', field_type='String',
                                                            mandatory=False, max_length=10),
                                                      Field(name='field3', label='My Field 2', field_type='Integer',
                                                            mandatory=False),
                                                     ]),
                                         Form(title='Secondform', 
                                              fields=[Field(name='field3', label='My Field 3', field_type='String',
                                                            mandatory=True,max_length=4),
                                                      Field(name='field4', label='My Field 4', field_type='String',
                                                            mandatory=False, max_length=10),
                                                      Link(name="vezica",label='Veza', field_type="Link",mandatory=False,
                                                           form="Firstform",link_type="1-*")
                                                     ]),
                                         Form(title='Thirdform', 
                                              fields=[Field(name='field1', label='My Field 3', field_type='String',
                                                            mandatory=True,max_length=4),
                                                      Field(name='field2', label='My Field 4', field_type='String',
                                                            mandatory=False, max_length=10),
                                                      Link(name="vezica",label='Veza', field_type="Link",mandatory=False,
                                                           form="Firstform",link_type="*-*"),
                                                      Link(name="vezica3",label='Veza', field_type="Link",mandatory=True,
                                                           form="Secondform",link_type="1-1"),
                                                      Field(name='field4', label='My Field 4', field_type='Float',
                                                            mandatory=True),
                                                      Field(name='field5', label='My Field 4', field_type='DateTime',
                                                            mandatory=False),
                                                     ]),
                                        ])

    def test_generator(self):
        generator.generate_app("test_gen", self.app_model)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()