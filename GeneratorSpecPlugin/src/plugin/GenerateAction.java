package plugin;

import java.awt.event.ActionEvent;
import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;

import javax.swing.JOptionPane;
import javax.swing.KeyStroke;

import plugin.analyzer.AnalyzeException;
import plugin.analyzer.ModelAnalyzer;

import com.nomagic.magicdraw.actions.MDAction;
import com.nomagic.magicdraw.core.Application;
import com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model;

/** Action that analyzes the model and serializes it to an xml file */
class GenerateAction extends MDAction
{
	private static final long serialVersionUID = 1L;

	public GenerateAction(String name)
	{
		super("GenerateAction", name, KeyStroke.getKeyStroke(KeyEvent.VK_G, InputEvent.CTRL_MASK), null);
	}

	@Override
	public void actionPerformed(ActionEvent evt)
	{
		Model root = Application.getInstance().getProject().getModel();
		
		if(root == null)
		{
			JOptionPane.showMessageDialog(null, "There is no model in the current project");
			return;
		}
		
		try
		{
			XMLUtil.toXmlFile(ModelAnalyzer.processPackage(root));
		}
		catch (AnalyzeException e)
		{
			JOptionPane.showMessageDialog(null, e.getMessage());
		}
	}
	
    /**
     * Defines when your action is available.
     */
	@Override
    public void updateState()
	{
		super.updateState();
        // This action is only available when a project is loaded
		setEnabled(Application.getInstance().getProject() != null);
    }
}
