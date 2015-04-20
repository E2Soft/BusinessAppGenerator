'''
Created on Mar 19, 2015

@author: PCX
'''
from generator.model import AppModel, Form, Field, Operation, Link, Package


f1 = Form(title='Firstform', display_name='First form',
                                              fields=[Field(name='field1', label='My Field 1', field_type='String',
                                                            mandatory=True,max_length=4, custom_validation=True),
                                                      Field(name='field2', label='My Field 2', field_type='String',
                                                            mandatory=False, max_length=10),
                                                      Field(name='field3', label='My Field 3', field_type='Integer',
                                                            mandatory=False, derived='REAL_TIME'),
                                                     ],
                                              operations=[Operation(name="searchFirstForm",field_type="Search",label="Search"),
                                                          Operation(name="customshit",label="Custom shit",field_type="Custom",param=True)],
                                              main_attribute='field1',
                                              tooltip = "Firstform is here"
                                              )

f2 = Form(title='Secondform', display_name='Second form',
                                              fields=[Field(name='field3', label='My Field 3', field_type='String',
                                                            mandatory=True,max_length=4),
                                                      Field(name='field4', label='My Field 4', field_type='String',
                                                            mandatory=False, max_length=10),
                                                      Link(name="vezica",label='Veza' , foreign_label='second veza', field_type="Link",mandatory=False,
                                                           form="Firstform",link_type="1-*")
                                                     ],
                                              operations=[Operation(name="searchSecondForm",field_type="Search",label="Search")],
                                              main_attribute='field3',
                                              tooltip = "Secondform is here"
                                              )

f3 = Form(title='Thirdform', display_name='Third form',
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
                                              main_attribute='field1',
                                              tooltip = "Thirdform is here"
                                              )

f4 = Form(title='Forthform', display_name='Forth form',
                                              fields=[Field(name='field1', label='My Field 1', field_type='String',
                                                            mandatory=True,max_length=4, custom_validation=True),
                                                      Field(name='field2', label='My Field 2', field_type='String',
                                                            mandatory=False, max_length=10),
                                                      Field(name='field3', label='My Field 3', field_type='Integer',
                                                            mandatory=False, derived='REAL_TIME'),
                                                     ],
                                              operations=[Operation(name="searchForthForm",field_type="Search",label="Search"),
                                                          Operation(name="customshit2",label="Custom shit 2",field_type="Custom",param=True)],
                                              main_attribute='field1',
                                              tooltip = "Forthform is here"
                                              )

f5 = Form(title='Fifthform', display_name='Fifth form',
                                              fields=[Field(name='field1', label='My Field 1', field_type='String',
                                                            mandatory=True,max_length=4, custom_validation=True),
                                                      Field(name='field2', label='My Field 2', field_type='String',
                                                            mandatory=False, max_length=10),
                                                      Field(name='field3', label='My Field 3', field_type='Integer',
                                                            mandatory=False, derived='REAL_TIME'),
                                                     ],
                                              operations=[Operation(name="searchFifthForm",field_type="Search",label="Search"),
                                                          Operation(name="customshit3",label="Custom shit 3",field_type="Custom",param=True)],
                                              main_attribute='field1',
                                              tooltip = "Fifthform is here"
                                              )

test_app_model = AppModel(app_name='My test app', 
                                  forms=[f1,f2,f3,f4,f5],packages=[Package(weight=1,forms=[f1,f2],label="Test1"),
                                                                   Package(weight=2,forms=[f3,f4],label="Test2",
                                                                           subpackages=[Package(weight=3,forms=[f5],label="Test3")]),
                                                                   ]
                          )

test_app_string = '''
<AppModel>
  <app_name>StorageApp</app_name>
  <forms>
    <Form>
      <title>StorageUser</title>
      <main_attribute>ime</main_attribute>
      <display_name>User</display_name>
      <tooltip>Allow viewing and manipulation of all Users</tooltip>
      <fields>
        <Field>
          <name>ime</name>
          <label>Name</label>
          <field_type>String</field_type>
          <mandatory>false</mandatory>
          <weight>1</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>prezime</name>
          <label>Last name</label>
          <field_type>String</field_type>
          <mandatory>false</mandatory>
          <weight>2</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>username</name>
          <label>Username</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>password</name>
          <label>Password</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>4</weight>
          <max_length>10</max_length>
        </Field>
      </fields>
      <operations>
        <Operation>
          <name>Search</name>
          <label>Search</label>
          <field_type>Search</field_type>
          <param>false</param>
        </Operation>
      </operations>
    </Form>
    <Form>
      <title>Item</title>
      <main_attribute>nazivArtikal</main_attribute>
      <display_name>Item</display_name>
      <tooltip>Allow viewing and manipulation of all Articles</tooltip>
      <fields>
        <Field>
          <name>nazivArtikal</name>
          <label>Name</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>kolicina</name>
          <label>Quantity</label>
          <field_type>Integer</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>100</max_length>
        </Field>
        <Field>
          <name>pojedinacnaCena</name>
          <label>Single item price</label>
          <field_type>Float</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>100</max_length>
        </Field>
        <Field>
          <name>sifraArtikal</name>
          <label>Code</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>4</weight>
          <max_length>20</max_length>
        </Field>
        <Link>
          <name>relationship3</name>
          <label>Declaration</label>
          <field_type>Link</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <form>Declaration</form>
          <link_type>1-*</link_type>
          <foreign_label>Item</foreign_label>
        </Link>
        <Link>
          <name>relationship9</name>
          <label>Category</label>
          <field_type>Link</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <form>Category</form>
          <link_type>1-*</link_type>
          <foreign_label>Item</foreign_label>
        </Link>
        <Link>
          <name>relationship5</name>
          <label>Shop</label>
          <field_type>Link</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <form>Shop</form>
          <link_type>*-*</link_type>
          <foreign_label>Item</foreign_label>
        </Link>
      </fields>
      <operations>
        <Operation>
          <name>Search</name>
          <label>Search</label>
          <field_type>Search</field_type>
          <param>false</param>
        </Operation>
        <Operation>
          <name>Popust</name>
          <label>Discount</label>
          <field_type>Custom</field_type>
          <param>false</param>
        </Operation>
        <Operation>
          <name>Popis</name>
          <label>Inventory document</label>
          <field_type>Custom</field_type>
          <param>false</param>
        </Operation>
      </operations>
    </Form>
    <Form>
      <title>Shop</title>
      <main_attribute>nazivRadnja</main_attribute>
      <display_name>Shop</display_name>
      <tooltip>Allow viewing and manipulation of all Stores</tooltip>
      <fields>
        <Field>
          <name>ulica</name>
          <label>Street</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>broj</name>
          <label>Number</label>
          <field_type>Integer</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>100</max_length>
        </Field>
        <Field>
          <name>grad</name>
          <label>City</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>nazivRadnja</name>
          <label>Name</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>30</max_length>
        </Field>
      </fields>
      <operations>
        <Operation>
          <name>Search</name>
          <label>Search</label>
          <field_type>Search</field_type>
          <param>false</param>
        </Operation>
      </operations>
    </Form>
    <Form>
      <title>Category</title>
      <main_attribute>naziv</main_attribute>
      <display_name>Category</display_name>
      <tooltip>Allow viewing and manipulation of all Categories</tooltip>
      <fields>
        <Field>
          <name>naziv</name>
          <label>Name</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>broj_artikala</name>
          <label>Number of items</label>
          <field_type>Integer</field_type>
          <mandatory>false</mandatory>
          <weight>2</weight>
          <derived>REAL_TIME</derived>
        </Field>
      </fields>
      <operations>
        <Operation>
          <name>Search</name>
          <label>Search</label>
          <field_type>Search</field_type>
          <param>false</param>
        </Operation>
      </operations>
    </Form>
    <Form>
      <title>State</title>
      <main_attribute>nazivDrzava</main_attribute>
      <display_name>State</display_name>
      <tooltip>Allow viewing and manipulation of all States</tooltip>
      <fields>
        <Field>
          <name>oznaka</name>
          <label>Code</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>3</max_length>
        </Field>
        <Field>
          <name>nazivDrzava</name>
          <label>Name</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>20</max_length>
          <custom_validation>true</custom_validation>
        </Field>
        <Field>
          <name>kontinentDrazava</name>
          <label>Continent</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>20</max_length>
        </Field>
      </fields>
      <operations>
        <Operation>
          <name>Search</name>
          <label>Search</label>
          <field_type>Search</field_type>
          <param>false</param>
        </Operation>
      </operations>
    </Form>
    <Form>
      <title>Manufacturer</title>
      <main_attribute>nazivProizvodjac</main_attribute>
      <display_name>Manufacturer</display_name>
      <tooltip>Allow viewing and manipulation of all Manufacturers</tooltip>
      <fields>
        <Field>
          <name>nazivProizvodjac</name>
          <label>Name</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>ulicaProizvodjac</name>
          <label>Street</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>brojProizvodjac</name>
          <label>Number</label>
          <field_type>Integer</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>gradProizvodjac</name>
          <label>City</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>4</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>telefonProizvodjac</name>
          <label>Phone</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>5</weight>
          <max_length>30</max_length>
        </Field>
      </fields>
      <operations>
        <Operation>
          <name>Search</name>
          <label>Search</label>
          <field_type>Search</field_type>
          <param>false</param>
        </Operation>
      </operations>
    </Form>
    <Form>
      <title>Declaration</title>
      <main_attribute>nazivDeklaracija</main_attribute>
      <display_name>Declaration</display_name>
      <tooltip>Allow viewing and manipulation of all Declarations</tooltip>
      <fields>
        <Field>
          <name>sifraDeklaracija</name>
          <label>Code</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>10</max_length>
        </Field>
        <Field>
          <name>datumUvoza</name>
          <label>Import date</label>
          <field_type>DateTime</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
        </Field>
        <Field>
          <name>nazivDeklaracija</name>
          <label>Name</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>20</max_length>
        </Field>
        <Link>
          <name>relationship4</name>
          <label>Importer</label>
          <field_type>Link</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <form>Importer</form>
          <link_type>1-*</link_type>
          <foreign_label>Declaration</foreign_label>
        </Link>
      </fields>
      <operations>
        <Operation>
          <name>Search</name>
          <label>Search</label>
          <field_type>Search</field_type>
          <param>false</param>
        </Operation>
      </operations>
    </Form>
    <Form>
      <title>Importer</title>
      <main_attribute>nazivUvoznik</main_attribute>
      <display_name>Importer</display_name>
      <tooltip>Allow viewing and manipulation of all Importers</tooltip>
      <fields>
        <Field>
          <name>nazivUvoznik</name>
          <label>Name</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>ulicaUvoznik</name>
          <label>Street</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>brojUvoznik</name>
          <label>Number</label>
          <field_type>Integer</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>100</max_length>
        </Field>
        <Field>
          <name>telefonUvoznik</name>
          <label>Phone</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>4</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>gradUvoznik</name>
          <label>City</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>5</weight>
          <max_length>20</max_length>
        </Field>
      </fields>
      <operations>
        <Operation>
          <name>Search</name>
          <label>Search</label>
          <field_type>Search</field_type>
          <param>false</param>
        </Operation>
      </operations>
    </Form>
  </forms>
  <packages>
    <Package>
      <name>Items</name>
      <label>Items</label>
      <weight>1</weight>
      <forms>
        <Form reference="../../../../forms/Form[2]"/>
        <Form reference="../../../../forms/Form[7]"/>
        <Form reference="../../../../forms/Form[8]"/>
        <Form reference="../../../../forms/Form[6]"/>
        <Form reference="../../../../forms/Form[4]"/>
      </forms>
      <packages/>
    </Package>
    <Package>
      <name>User</name>
      <label>User</label>
      <weight>2</weight>
      <forms>
        <Form reference="../../../../forms/Form"/>
        <Form reference="../../../../forms/Form[3]"/>
        <Form reference="../../../../forms/Form[5]"/>
      </forms>
      <packages/>
    </Package>
  </packages>
</AppModel>
'''
