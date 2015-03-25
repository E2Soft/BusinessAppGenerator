package plugin;

import com.nomagic.actions.NMAction;
import com.nomagic.magicdraw.actions.ActionsConfiguratorsManager;

public class GeneratorPlugin extends com.nomagic.magicdraw.plugins.Plugin
{
	public void init() 
	{
		// Creating submenu in the MagicDraw main menu 	
		ActionsConfiguratorsManager manager = ActionsConfiguratorsManager.getInstance();		
		manager.addMainMenuConfigurator(new MainMenuConfigurator(getSubmenuActions()));
	}

	private NMAction[] getSubmenuActions()
	{
	   return new NMAction[]{new GenerateAction("Generate app specification"),};
	}
	
	public boolean close()
	{
		return true;
	}
	
	public boolean isSupported()
	{				
		return true;
	}
}
