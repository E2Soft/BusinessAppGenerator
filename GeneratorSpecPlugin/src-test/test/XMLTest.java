package test;

import java.io.OutputStreamWriter;

import plugin.XMLUtil;
import plugin.model.TestClass;
import plugin.model.TestClassSecond;
import plugin.model.TestClassThird;

public class XMLTest
{
	public static void main(String[] args) throws Exception
	{
		TestClassThird third = new TestClassThird("1", 1, 2, 3);
		TestClass t = new TestClass("3", 1,2,34,"dfg", new TestClassSecond("2", 4, 4, 5, "fgh", third), third);
		
		XMLUtil.toXmlStream(t, new OutputStreamWriter(System.out));
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
