package plugin.model;

import java.util.List;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("Form")
public class Form
{
	String title;
	List<Field> fields;
	List<Operation> operations;
	public Form(String title, List<Field> fields, List<Operation> operations)
	{
		super();
		this.title = title;
		this.fields = fields;
		this.operations = operations;
	}
}
