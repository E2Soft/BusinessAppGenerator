'''
Created on Mar 19, 2015

@author: PCX
'''
from test.model import AppModel, Form, Field, Operation, Link

test_app_model = AppModel(app_name='My test app', 
                                  forms=[Form(title='Firstform', display_name='First form',
                                              fields=[Field(name='field1', label='My Field 1', field_type='String',
                                                            mandatory=True,max_length=4),
                                                      Field(name='field2', label='My Field 2', field_type='String',
                                                            mandatory=False, max_length=10),
                                                      Field(name='field3', label='My Field 3', field_type='Integer',
                                                            mandatory=False),
                                                     ],
                                              operations=[Operation(name="searchFirstForm",field_type="Search",label="Search"),
                                                          Operation(name="customshit",label="Custom shit",field_type="Custom",param=True)],
                                              main_attribute='field1'
                                              ),
                                         Form(title='Secondform', display_name='Second form',
                                              fields=[Field(name='field3', label='My Field 3', field_type='String',
                                                            mandatory=True,max_length=4),
                                                      Field(name='field4', label='My Field 4', field_type='String',
                                                            mandatory=False, max_length=10),
                                                      Link(name="vezica",label='Veza' , foreign_label='second veza', field_type="Link",mandatory=False,
                                                           form="Firstform",link_type="1-*")
                                                     ],
                                              operations=[Operation(name="searchSecondForm",field_type="Search",label="Search")],
                                              main_attribute='field3'
                                              ),
                                         Form(title='Thirdform', display_name='Third form',
                                              fields=[Field(name='field1', label='My Field 1', field_type='String',
                                                            mandatory=True,max_length=4),
                                                      Field(name='field2', label='My Field 2', field_type='String',
                                                            mandatory=False, max_length=10, weight=1),
                                                      Link(name="vezica",label='Veza', foreign_label='third veza', field_type="Link",mandatory=False,
                                                           form="Firstform",link_type="*-*", weight=3),
                                                      Link(name="vezica3",label='Veza3', foreign_label='third veza', field_type="Link",mandatory=True,
                                                           form="Secondform",link_type="1-1", weight=2),
                                                      Field(name='field4', label='My Field 4', field_type='Float',
                                                            mandatory=True, weight=4),
                                                      Field(name='field5', label='My Field 5', field_type='DateTime',
                                                            mandatory=False, weight=4),
                                                     ],
                                              operations=[Operation(name="searchThirdForm",field_type="Search",label="Search"),
                                                          Operation(name="custommethod",label="Custom shit",field_type="Custom")],
                                              main_attribute='field1'
                                              ),
                                        ])