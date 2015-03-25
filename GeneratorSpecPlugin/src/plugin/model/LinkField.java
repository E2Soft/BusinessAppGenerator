package plugin.model;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("Link")
public class LinkField extends Field
{
	String form;
	String link_type;
	String foreign_label;
	public LinkField(String name, String label, String field_type, Boolean mandatory, Integer weight, String form, String link_type, String foreign_label)
	{
		super(name, label, field_type, mandatory, weight);
		this.form=form;
		this.link_type=link_type;
		this.foreign_label = foreign_label;
	}
}
