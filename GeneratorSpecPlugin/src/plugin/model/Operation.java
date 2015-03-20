package plugin.model;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("Operation")
public class Operation
{
    String name;
    String label;
    String field_type;
    boolean param;
	public Operation(String name, String label, String field_type, boolean param)
	{
		super();
		this.name = name;
		this.label = label;
		this.field_type = field_type;
		this.param = param;
	}
}
