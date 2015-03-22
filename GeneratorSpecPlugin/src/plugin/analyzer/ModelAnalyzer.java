package plugin.analyzer;

import plugin.model.AppModel;

import com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package;


/** Model Analyzer takes necessary metadata from the MagicDraw model and puts it in 
 * the intermediate data structure. 
 */ 
public class ModelAnalyzer
{
	public static AppModel processPackage(Package pack) throws AnalyzeException
	{
		//Recursive procedure that extracts data from package elements and stores it in the intermediate data structure

		if(pack.getName() == null)
		{
			throw new AnalyzeException("Packages must have names!");
		}
		
		for(Element ownedElement : pack.getOwnedElement())
		{
			if(ownedElement instanceof Class)
			{
				Class cl = (Class)ownedElement;
				
			}

			if(ownedElement instanceof Enumeration)
			{
				Enumeration en = (Enumeration)ownedElement;
				
			}
		}

		for(Element ownedElement : pack.getOwnedElement())
		{
			if(ownedElement instanceof Package)
			{					
				Package ownedPackage = (Package)ownedElement;
				if (StereotypesHelper.getAppliedStereotypeByString(ownedPackage, "BusinessApp") != null)
				{
					processPackage(ownedPackage);
				}
			}
		}
		
		return null;
	}
/*
	private FMClass getClassData(Class cl, String packageName) throws AnalyzeException {
		if (cl.getName() == null) 
			throw new AnalyzeException("Classes must have names!");

		FMClass fmClass = new FMClass(cl.getName(), packageName, cl.getVisibility().toString());
		Iterator<Property> it = ModelHelper.attributes(cl);
		while (it.hasNext()) {
			Property p = it.next();
			FMProperty prop = getPropertyData(p, cl);
			fmClass.addProperty(prop);	
		}	
		return fmClass;
	}

	private FMProperty getPropertyData(Property p, Class cl) throws AnalyzeException {
		String attName = p.getName();
		if (attName == null) 
			throw new AnalyzeException("Properties of the class: " + cl.getName() +
					" must have names!");
		Type attType = p.getType();
		if (attType == null)
			throw new AnalyzeException("Property " + cl.getName() + "." +
					p.getName() + " must have type!");

		String typeName = attType.getName();
		if (typeName == null)
			throw new AnalyzeException("Type ot the property " + cl.getName() + "." +
					p.getName() + " must have name!");		

		int lower = p.getLower();
		int upper = p.getUpper();

		FMProperty prop = new FMProperty(attName, typeName, p.getVisibility().toString(), 
				lower, upper);
		return prop;		
	}	

	private FMEnumeration getEnumerationData(Enumeration enumeration, String packageName) throws AnalyzeException {
		FMEnumeration fmEnum = new FMEnumeration(enumeration.getName(), packageName);
		List<EnumerationLiteral> list = enumeration.getOwnedLiteral();
		for (int i = 0; i < list.size() - 1; i++) {
			EnumerationLiteral literal = list.get(i);
			if (literal.getName() == null)  
				throw new AnalyzeException("Items of the enumeration " + enumeration.getName() +
						" must have names!");
			fmEnum.addValue(literal.getName());
		}
		return fmEnum;
	}	
*/

}
