package test;

import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

import plugin.XMLUtil;
import plugin.model.AppModel;
import plugin.model.Field;
import plugin.model.Form;
import plugin.model.FormField;
import plugin.model.LinkField;

public class XMLTest
{
	public static void main(String[] args) throws Exception
	{
		List<Form> forms = new ArrayList<>();
		List<Field> fields;
		
		fields = new ArrayList<>();
		fields.add(new FormField("polje1", "Polje 1", "int", true, 5));
		fields.add(new FormField("polje2", "Polje 2", "string", false, 5));
		
		Form form1 = new Form("Form 1", fields);
		
		fields = new ArrayList<>();
		fields.add(new FormField("polje3", "Polje 3", "int", true, 5));
		fields.add(new FormField("polje4", "Polje 4", "string", false, 5));
		fields.add(new LinkField("forma1link", "Forma 1", "Link", true, form1, "1-1"));
		
		Form form2 = new Form("Form 2", fields);
		
		fields = new ArrayList<>();
		fields.add(new FormField("polje3", "Polje 3", "int", true, 5));
		fields.add(new FormField("polje4", "Polje 4", "string", false, 5));
		fields.add(new LinkField("forma2link", "Forma 2", "Link", true, form2, "1-1"));
		
		Form form3 = new Form("Form 2", fields);
		
		forms.add(form1);
		forms.add(form2);
		forms.add(form3);
		
		AppModel a = new AppModel("MyApp", forms);
		
		XMLUtil.toXmlStream(a, new OutputStreamWriter(System.out));
	}
	
	/*
	public TestPackageGeneration(){
		
	}
	
	private void initModel() {		
		
		List<FMClass> classes = FMModel.getInstance().getClasses();
		
		classes.clear();
		
		FMClass cl = new FMClass ("Preduzece", "ejb.orgsema", "public");
		cl.addProperty(new FMProperty("sifraPreduzeca", "String", "private", 1, 1));
		cl.addProperty(new FMProperty("nazivPreduzeca", "String", "private", 1, 1));
		
		classes.add(cl);
		
		cl = new FMClass ("Materijal", "ejb.magacin", "public");
		cl.addProperty(new FMProperty("sifraMaterijala", "String", "private", 1, 1));
		cl.addProperty(new FMProperty("nazivMaterijala", "String", "private", 1, 1));
		cl.addProperty(new FMProperty("slozen", "Boolean", "private", 1, 1));
		
		classes.add(cl);
		
		cl = new FMClass ("Odeljenje", "ejb.orgsema", "public");
		cl.addProperty(new FMProperty("sifra", "String", "private", 1, 1));
		cl.addProperty(new FMProperty("naziv", "String", "private", 1, 1));
		
		classes.add(cl);
		
		cl = new FMClass ("Osoba", "ejb", "public");
		cl.addProperty(new FMProperty("prezime", "String", "private", 1, 1));		
		cl.addProperty(new FMProperty("ime", "String", "private", 1, 1));
		cl.addProperty(new FMProperty("datumRodjenja", "Date", "private", 0, 1));
		cl.addProperty(new FMProperty("clanoviPorodice", "Osoba", "private", 0, -1));	
		cl.addProperty(new FMProperty("vestina", "String", "private", 1, 3));
		
		classes.add(cl);
		
		cl = new FMClass ("Kartica", "ejb.magacin.kartica", "public");
		cl.addProperty(new FMProperty("sifraKartice", "String", "private", 1, 1));
		cl.addProperty(new FMProperty("nazivKartice", "String", "private", 1, 1));
		
		classes.add(cl);		
	}
	
	public void testGenerator() {
		initModel();		
		GeneratorOptions go = ProjectOptions.getProjectOptions().getGeneratorOptions().get("EJBGenerator");	
		//EJBGenerator g = new EJBGenerator(go);
		//g.generate();
	}
	*/
}
