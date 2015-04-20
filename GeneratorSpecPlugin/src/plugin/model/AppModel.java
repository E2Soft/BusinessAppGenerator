package plugin.model;

import java.util.List;

import com.thoughtworks.xstream.annotations.XStreamAlias;

@XStreamAlias("AppModel")
public class AppModel
{
	String app_name;
	List<Form> forms;
	List<Package> packages;
	public AppModel(String app_name, List<Form> forms, List<Package> packages)
	{
		super();
		this.app_name = app_name;
		this.forms = forms;
		this.packages = packages;
	}
}
