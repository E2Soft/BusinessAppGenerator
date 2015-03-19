package plugin.model;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("FormField")
public class FormField extends Field
{
	int max_length;
	public FormField(String name, String label, String field_type, boolean mandatory, int max_length)
	{
		super(name, label, field_type, mandatory);
		this.max_length = max_length;
	}
}
