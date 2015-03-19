package plugin.model;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("LinkField")
public class LinkField extends Field
{
	Form form;
	String link_type;
	public LinkField(String name, String label, String field_type,boolean mandatory, Form form, String link_type)
	{
		super(name, label, field_type, mandatory);
		this.form=form;
		this.link_type=link_type;
	}
}
