package plugin.model;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("Field")
public class FormField extends Field
{
	Integer max_length;
	Boolean custom_validation;
	public FormField(String name, String label, String field_type, Boolean mandatory, Integer weight, Integer max_length, Boolean custom_validation)
	{
		super(name, label, field_type, mandatory, weight);
		this.max_length = max_length;
		this.custom_validation = custom_validation;
	}
}
