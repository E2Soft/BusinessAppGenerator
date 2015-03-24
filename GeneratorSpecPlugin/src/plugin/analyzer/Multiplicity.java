package plugin.analyzer;

import java.util.HashMap;
import java.util.Map;

public class Multiplicity
{
	private String min;
	private String max;
	private static Map<String, Multiplicity> multiplicities;
	
	static
	{
		multiplicities = new HashMap<String, Multiplicity>();
		multiplicities.put("0..1", new Multiplicity("0", "1"));
		multiplicities.put("1..1", new Multiplicity("1", "1"));
		multiplicities.put("0..*", new Multiplicity("0", "*"));
		multiplicities.put("1..*", new Multiplicity("1", "*"));
		multiplicities.put("1", new Multiplicity("1", "1"));
		multiplicities.put("*", new Multiplicity("0", "*"));
	}
	
	public static Multiplicity get(String multiplicity)
	{
		return multiplicities.get(multiplicity);
	}
	
	private Multiplicity(String min, String max)
	{
		this.min = min;
		this.max = max;
	}

	public String getMin()
	{
		return min;
	}

	public String getMax()
	{
		return max;
	}
	
	public String toString()
	{
		return min+".."+max;
	}
	
	public boolean isMandatory()
	{
		return "1".equals(min);
	}
}
