package plugin.model;

import java.util.List;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("Package")
public class Package
{
	String name;
	String label;
	Integer weight;
	List<Form> forms;
	List<Package> packages;
	public Package(String name, String label, Integer weight, List<Form> forms, List<Package> packages)
	{
		super();
		this.name = name;
		this.label = label;
		this.weight = weight;
		this.forms = forms;
		this.packages = packages;
	}
	public List<Form> getForms()
	{
		return forms;
	}
	public List<Package> getPackages()
	{
		return packages;
	}
}
