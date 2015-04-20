package plugin;

import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;

import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
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
			XMLUtil.toXmlFile(new ModelAnalyzer().processApplication(root));
			JOptionPane.showMessageDialog(null, "Project generated.");
		}
		catch (AnalyzeException e)
		{
			JOptionPane.showMessageDialog(null, e.getMessage());
		}
		catch(Exception e)
		{
			StringBuilder sb = new StringBuilder("Error: ");
            sb.append(e.getMessage());
            sb.append("\n");
            for (StackTraceElement ste : e.getStackTrace()) {
                sb.append(ste.toString());
                sb.append("\n");
            }
            JTextArea jta = new JTextArea(sb.toString());
            @SuppressWarnings("serial")
			JScrollPane jsp = new JScrollPane(jta){
                @Override
                public Dimension getPreferredSize() {
                    return new Dimension(480, 320);
                }
            };
            
            JOptionPane.showMessageDialog(null, jsp, "Error", JOptionPane.ERROR_MESSAGE);
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
