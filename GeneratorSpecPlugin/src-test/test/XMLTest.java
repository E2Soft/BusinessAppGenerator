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
import plugin.model.Operation;

import plugin.model.Package;

public class XMLTest
{
	public static void main(String[] args) throws Exception
	{
		List<Form> forms = new ArrayList<Form>();
		List<Field> fields;
		List<Operation> operations;
		
		fields = new ArrayList<Field>();
		fields.add(new FormField("polje1", "Polje 1", "int", true, 5, 1, false, null));
		fields.add(new FormField("polje2", "Polje 2", "string", false, 5, 2, true, null));
		
		operations = new ArrayList<Operation>();
		operations.add(new Operation("Operation1", "Operation1", "nesto", true));
		operations.add(new Operation("Operation2", "Operation2", "nesto2", false));
		
		Form form1 = new Form("Form_1", "polje1", "Form 1", "tooltip 1", fields, operations);
		
		fields = new ArrayList<Field>();
		fields.add(new FormField("polje3", "Polje 3", "int", true, 5, 1, false, null));
		fields.add(new FormField("polje4", "Polje 4", "string", false, 5, 2, false, null));
		fields.add(new LinkField("forma1link", "Forma 1", "Link", true, 3, "Form_1", "1-1", "f veza 1"));
		
		Form form2 = new Form("Form_2", "polje3", "Form 2", "tooltip 1", fields, new ArrayList<Operation>());
		
		fields = new ArrayList<Field>();
		fields.add(new FormField("polje3", "Polje 3", "int", true, 5, 1, false, null));
		fields.add(new FormField("polje4", "Polje 4", "string", false, 5, 2, false, null));
		fields.add(new LinkField("forma2link", "Forma 2", "Link", true, 3, "Form_2", "1-1", "f veza 2"));
		
		Form form3 = new Form("Form_3", "polje3", "Form 3", "tooltip 1", fields, new ArrayList<Operation>());
		
		forms.add(form1);
		forms.add(form2);
		forms.add(form3);
		
		List<Package> packages = new ArrayList<Package>();
		
		List<Form> packForms = new ArrayList<Form>();
		packForms.add(form1);
		packForms.add(form2);
		packages.add(new Package("Package1", "Package 1", 1, packForms, new ArrayList<Package>()));
		
		packForms = new ArrayList<Form>();
		packForms.add(form3);
		packages.add(new Package("Package2", "Package 2", 2, packForms, new ArrayList<Package>()));
		
		AppModel a = new AppModel("My App", forms, packages);
		
		XMLUtil.toXmlStream(a, new OutputStreamWriter(System.out));
	}
}
