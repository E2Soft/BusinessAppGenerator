package plugin.model;

import java.util.List;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("Form")
public class Form
{
	String title;
	String main_attribute;
	String display_name;
	List<Field> fields;
	List<Operation> operations;
	public Form(String title, String main_attribute, String display_name, List<Field> fields, List<Operation> operations)
	{
		super();
		this.title = title;
		this.main_attribute = main_attribute;
		this.display_name = display_name;
		this.fields = fields;
		this.operations = operations;
	}
}
