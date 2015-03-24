package plugin.model;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("Operation")
public class Operation
{
    String name;
    String label;
    String field_type;
    Boolean param;
	public Operation(String name, String label, String field_type, Boolean param)
	{
		super();
		this.name = name;
		this.label = label;
		this.field_type = field_type;
		if (param == null)
		{
			this.param = false;
		}
		else
		{
			this.param = param;
		}
	}
}
