package plugin.model;

public abstract class Field
{
	String name;
    String label;
	String field_type;
    boolean mandatory;
	public Field(String name, String label, String field_type, boolean mandatory)
	{
		super();
		this.name = name;
		this.label = label;
		this.field_type = field_type;
		this.mandatory = mandatory;
	}
}
