package plugin.model;

import java.util.List;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("Form")
public class Form
{
	String title;
	List<Field> fields;
	public Form(String title, List<Field> fields)
	{
		super();
		this.title = title;
		this.fields = fields;
	}
}
