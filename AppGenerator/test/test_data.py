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
                                                                   Package(weight=2,forms=[f3,f4],label="Test2"),
                                                                   Package(weight=3,forms=[f5],label="Test3")])

test_app_string = '''
<AppModel>
  <app_name>StorageDBModel</app_name>
  <forms>
    <Form>
      <title>Drzava</title>
      <main_attribute>nazivDrzava</main_attribute>
      <display_name>Drzava</display_name>
      <fields>
        <Field>
          <name>oznaka</name>
          <label>Oznaka</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>3</max_length>
        </Field>
        <Field>
          <name>nazivDrzava</name>
          <label>Naziv</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>20</max_length>
          <custom_validation>true</custom_validation>
        </Field>
        <Field>
          <name>kontinentDrazava</name>
          <label>Kontinent</label>
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
      <title>Korisnik</title>
      <main_attribute>ime</main_attribute>
      <display_name>Korisnik</display_name>
      <fields>
        <Field>
          <name>ime</name>
          <label>Ime</label>
          <field_type>String</field_type>
          <mandatory>false</mandatory>
          <weight>1</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>prezime</name>
          <label>Prezime</label>
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
        <Link>
          <name>relationship6</name>
          <label>Radnja</label>
          <field_type>Link</field_type>
          <mandatory>false</mandatory>
          <weight>1</weight>
          <form>Radnja</form>
          <link_type>1-*</link_type>
          <foreign_label>Korisnik</foreign_label>
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
      <title>Proizvodjac</title>
      <main_attribute>nazivProizvodjac</main_attribute>
      <display_name>Proizvodjac</display_name>
      <fields>
        <Field>
          <name>nazivProizvodjac</name>
          <label>Naziv</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>ulicaProizvodjac</name>
          <label>Ulica</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>brojProizvodjac</name>
          <label>Broj</label>
          <field_type>Integer</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>gradProizvodjac</name>
          <label>Grad</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>4</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>telefonProizvodjac</name>
          <label>Telefon</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>5</weight>
          <max_length>30</max_length>
        </Field>
        <Link>
          <name>drzavaProizvodjaca</name>
          <label>Drzava</label>
          <field_type>Link</field_type>
          <mandatory>false</mandatory>
          <weight>1</weight>
          <form>Drzava</form>
          <link_type>1-*</link_type>
          <foreign_label>Proizvodjac</foreign_label>
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
      <title>Artikal</title>
      <main_attribute>nazivArtikal</main_attribute>
      <display_name>Artikal</display_name>
      <fields>
        <Field>
          <name>nazivArtikal</name>
          <label>Naziv</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>kolicina</name>
          <label>Kolicina</label>
          <field_type>Integer</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>100</max_length>
        </Field>
        <Field>
          <name>pojedinacnaCena</name>
          <label>Pojedinacna cena</label>
          <field_type>Float</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>100</max_length>
        </Field>
        <Field>
          <name>sifraArtikal</name>
          <label>Sifra</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>4</weight>
          <max_length>20</max_length>
        </Field>
        <Link>
          <name>relationship3</name>
          <label>Deklaracija</label>
          <field_type>Link</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <form>Deklaracija</form>
          <link_type>1-*</link_type>
          <foreign_label>Artikal</foreign_label>
        </Link>
        <Link>
          <name>relationship5</name>
          <label>Radnja</label>
          <field_type>Link</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <form>Radnja</form>
          <link_type>*-*</link_type>
          <foreign_label>Artikal</foreign_label>
        </Link>
        <Link>
          <name>relationship9</name>
          <label>Kategorija</label>
          <field_type>Link</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <form>Kategorija</form>
          <link_type>1-*</link_type>
          <foreign_label>Artikal</foreign_label>
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
          <label>Uracunaj popust</label>
          <field_type>Custom</field_type>
          <param>false</param>
        </Operation>
      </operations>
    </Form>
    <Form>
      <title>Radnja</title>
      <main_attribute>nazivRadnja</main_attribute>
      <display_name>Radnja</display_name>
      <fields>
        <Field>
          <name>ulica</name>
          <label>Ulica</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>broj</name>
          <label>Broj</label>
          <field_type>Integer</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>100</max_length>
        </Field>
        <Field>
          <name>grad</name>
          <label>Grad</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>nazivRadnja</name>
          <label>Naziv radnje</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>30</max_length>
        </Field>
        <Link>
          <name>relationship7</name>
          <label>Drzava</label>
          <field_type>Link</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <form>Drzava</form>
          <link_type>1-*</link_type>
          <foreign_label>Radnja</foreign_label>
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
      <title>Kategorija</title>
      <main_attribute>naziv</main_attribute>
      <display_name>Kategorija</display_name>
      <fields>
        <Field>
          <name>naziv</name>
          <label>Naziv</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>broj_artikala</name>
          <label>Broj artikala</label>
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
      <title>Uvoznik</title>
      <main_attribute>nazivUvoznik</main_attribute>
      <display_name>Uvoznik</display_name>
      <fields>
        <Field>
          <name>nazivUvoznik</name>
          <label>Naziv</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>ulicaUvoznik</name>
          <label>Ulica</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>20</max_length>
        </Field>
        <Field>
          <name>brojUvoznik</name>
          <label>Broj</label>
          <field_type>Integer</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
          <max_length>100</max_length>
        </Field>
        <Field>
          <name>telefonUvoznik</name>
          <label>Telefon</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>4</weight>
          <max_length>30</max_length>
        </Field>
        <Field>
          <name>gradUvoznik</name>
          <label>Grad</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>5</weight>
          <max_length>20</max_length>
        </Field>
        <Link>
          <name>drzavaUvoznika</name>
          <label>Drzava</label>
          <field_type>Link</field_type>
          <mandatory>false</mandatory>
          <weight>1</weight>
          <form>Drzava</form>
          <link_type>1-*</link_type>
          <foreign_label>Uvoznik</foreign_label>
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
      <title>Deklaracija</title>
      <main_attribute>nazivDeklaracija</main_attribute>
      <display_name>Deklaracija</display_name>
      <fields>
        <Field>
          <name>sifraDeklaracija</name>
          <label>Sifra</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <max_length>10</max_length>
        </Field>
        <Field>
          <name>datumUvoza</name>
          <label>Datum Uvoza</label>
          <field_type>DateTime</field_type>
          <mandatory>true</mandatory>
          <weight>3</weight>
        </Field>
        <Field>
          <name>nazivDeklaracija</name>
          <label>Naziv</label>
          <field_type>String</field_type>
          <mandatory>true</mandatory>
          <weight>2</weight>
          <max_length>20</max_length>
        </Field>
        <Link>
          <name>relationship4</name>
          <label>Uvoznik</label>
          <field_type>Link</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <form>Uvoznik</form>
          <link_type>1-*</link_type>
          <foreign_label>Deklaracija</foreign_label>
        </Link>
        <Link>
          <name>relationship8</name>
          <label>Drzava</label>
          <field_type>Link</field_type>
          <mandatory>true</mandatory>
          <weight>1</weight>
          <form>Drzava</form>
          <link_type>1-*</link_type>
          <foreign_label>Deklaracija</foreign_label>
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
  </forms>
</AppModel>
'''
