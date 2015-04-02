package plugin.analyzer;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import plugin.model.AppModel;
import plugin.model.Field;
import plugin.model.Form;
import plugin.model.FormField;
import plugin.model.LinkField;

import com.nomagic.uml2.ext.jmi.helpers.ModelHelper;
import com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property;
import com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype;


/** Model Analyzer takes necessary metadata from the MagicDraw model and puts it in 
 * the intermediate data structure. 
 */ 
public class ModelAnalyzer
{
	Map<String, Form> allForms;
	
	public ModelAnalyzer()
	{
		allForms = new HashMap<String, Form>();
	}
	
	public AppModel processApplication(Package root) throws AnalyzeException
	{
		for(Element ownedElementApp : root.getOwnedElement())
		{
			if(ownedElementApp instanceof Package && isStereotypeAplied(ownedElementApp, "BusinessApp"))
			{
				Package app = (Package)ownedElementApp;
				
				String app_name = app.getName();
				
				List<plugin.model.Package> allPackages = processSubPackages(app);
				
				processLinks(app);
				
				List<Form> allFormModels = getAllForms(allPackages);
				
				return new AppModel(app_name, allFormModels, allPackages);
			}
		}
		
		throw new AnalyzeException("No package annotated with BusinessApp stereotype.");
	}
	
	private List<Form> getAllForms(List<plugin.model.Package> packages)
	{
		List<Form> allForms = new ArrayList<Form>();
		for(plugin.model.Package pack : packages)
		{
			allForms.addAll(pack.getForms());
			allForms.addAll(getAllForms(pack.getPackages()));
		}
		return allForms;
	}
	
	private List<plugin.model.Package> processSubPackages(Package pack) throws AnalyzeException
	{
		List<plugin.model.Package> packages = new ArrayList<plugin.model.Package>();
		for(Element ownedElementPackage : pack.getOwnedElement())
		{
			if(ownedElementPackage instanceof Package && isStereotypeAplied(ownedElementPackage, "Package"))
			{
				Package subPack = (Package)ownedElementPackage;
				plugin.model.Package packageModel = processPackage(subPack);
				packages.add(packageModel);
			}
		}
		return packages;
	}

	public plugin.model.Package processPackage(Package pack) throws AnalyzeException
	{
		//Recursive procedure that extracts data from package elements and stores it in the intermediate data structure
		
		String name = pack.getName();
		if(name == null)
		{
			throw new AnalyzeException("Packages must have names!");
		}
		
		String label = getStringValue(pack, "Package", "label");
		Integer weight = getIntegerValue(pack, "Package", "weight");
		
		List<Form> forms = processForms(pack);
		
		List<plugin.model.Package> packages = processSubPackages(pack);
		
		return new plugin.model.Package(name, label, weight, forms, packages);
	}

	private List<Form> processForms(Package pack) throws AnalyzeException
	{
		List<Form> forms = new ArrayList<Form>();
		
		for(Element ownedElement : pack.getOwnedElement())
		{
			// forme
			if(ownedElement instanceof Class && isStereotypeAplied(ownedElement, "Form"))
			{
				Class form = (Class)ownedElement;
				
				String display_name = getStringValue(form, "Form", "label");
				
				if(display_name == null) 
				{
					throw new AnalyzeException("Encountered a class with no name.");
				}
				
				String title = form.getName().replace(" ", "_");
				
				String main_attribute = getStringValue(form, "Form", "main_attribute");
				Boolean has_search = getBooleanValue(form, "Form", "has_search");
				
				List<Field> fields = new ArrayList<Field>();
				
				List<plugin.model.Operation> operations = new ArrayList<plugin.model.Operation>();
				
				if(has_search != null && has_search)
				{
					operations.add(new plugin.model.Operation("Search", "Search", "Search", false));
				}
				
				for(Property prop : form.getAttribute())
				{
					if(isStereotypeAplied(prop, "Field"))
					{
						String label = getStringValue(prop, "Field", "label");
						String field_type = getEnumerationValue(prop, "Field", "field_type");
						Boolean mandatory = getBooleanValue(prop, "Field", "mandatory");
						Integer weight = getIntegerValue(prop, "Field", "weight");
						Integer max_length = getIntegerValue(prop, "Field", "max_length");
						Boolean custom_validation = getBooleanValue(prop, "Field", "custom_validation");
						String derived = getEnumerationValue(prop, "Field", "derived");
						
						fields.add(new FormField(prop.getName(), label, field_type, mandatory, weight, max_length, custom_validation, derived));
					}
				}
				
				for(Operation operation : form.getOwnedOperation())
				{
					if(isStereotypeAplied(operation, "Operation"))
					{
						String label = getStringValue(operation, "Operation", "label");
						Boolean param = getBooleanValue(operation, "Operation", "param");
						
						operations.add(new plugin.model.Operation(operation.getName(), label, "Custom", param));
					}
				}
				
				Form newForm = new Form(title, main_attribute, display_name, fields, operations);
				forms.add(newForm);
				allForms.put(form.getName(), newForm);
			}
		}
		
		return forms;
	}

	private void processLinks(Package pack) throws AnalyzeException 
	{
		for(Element ownedElement : pack.getOwnedElement())
		{
			if(ownedElement instanceof Association && isStereotypeAplied(ownedElement, "Link"))
			{
				processLink((Association)ownedElement);
			}
			else if(ownedElement instanceof Package && isStereotypeAplied(ownedElement, "Package"))
			{
				processLinks((Package)ownedElement);
			}
		}
	}
	
	private void processLink(Association link) throws AnalyzeException
	{
		String linkName = link.getName();
		String label = getStringValue(link, "Link", "label");
		Integer weight = getIntegerValue(link, "Link", "weight");
		String foreign_label = getStringValue(link, "Link", "foreign_label");
		
		Class firstForm = null;
		Class secondForm = null;
		Multiplicity firstMultiplicity = null;
		Multiplicity secondMultiplicity = null;
		
		for(Property linkEnd : link.getMemberEnd())
		{
			if(linkEnd.isNavigable())
			{
				secondForm = (Class) linkEnd.getType();
				secondMultiplicity = Multiplicity.get(ModelHelper.getMultiplicity(linkEnd));
			}
			else
			{
				firstForm = (Class) linkEnd.getType();
				firstMultiplicity = Multiplicity.get(ModelHelper.getMultiplicity(linkEnd));
			}
		}
		
		if(firstForm == null)
		{
			throw new AnalyzeException("All members of an association <"+linkName+"> are navigable. Exactly one member should be navigable.");
		}
		else if(secondForm == null)
		{
			throw new AnalyzeException("No members of an association <"+linkName+"> are navigable. Exactly one member should be navigable.");
		}
		
		String link_type = firstMultiplicity.getMax()+"-"+secondMultiplicity.getMax();
		
		LinkField newLink = new LinkField(linkName, label, "Link", firstMultiplicity.isMandatory(), weight, firstForm.getName(), link_type, foreign_label);

		allForms.get(secondForm.getName()).getFields().add(newLink);
	}
	
	private Boolean getBooleanValue(Element element, String stereotype, String tag)
	{
		return (Boolean) getObjectValue(element, stereotype, tag);
	}
	
	private String getStringValue(Element element, String stereotype, String tag)
	{
		return (String) getObjectValue(element, stereotype, tag);
	}
	
	private String getEnumerationValue(Element element, String stereotype, String tag)
	{
		EnumerationLiteral enumeration = (EnumerationLiteral)  getObjectValue(element, stereotype, tag);
		if(enumeration != null)
		{
			return enumeration.getName();
		}
		else
		{
			return null;
		}
	}
	
	private Integer getIntegerValue(Element element, String stereotype, String tag)
	{
		return (Integer) getObjectValue(element, stereotype, tag);
	}
	
	private Object getObjectValue(Element element, String stereotype, String tag)
	{
		Stereotype st = StereotypesHelper.getAppliedStereotypeByString(element, stereotype);
		return StereotypesHelper.getStereotypePropertyFirst(element, st, tag);
	}
	
	private boolean isStereotypeAplied(Element element, String stereotype)
	{
		return StereotypesHelper.isElementStereotypedBy(element, stereotype);
	}
}
