package plugin.model;

public abstract class Field
{
	String name;
    String label;
	String field_type;
    boolean mandatory;
    int weight;
	public Field(String name, String label, String field_type, boolean mandatory, int weight)
	{
		super();
		this.name = name;
		this.label = label;
		this.field_type = field_type;
		this.mandatory = mandatory;
		this.weight = weight;
	}
}
