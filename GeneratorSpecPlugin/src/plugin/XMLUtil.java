package plugin;

import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;

import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.naming.NoNameCoder;
import com.thoughtworks.xstream.io.xml.DomDriver;

public class XMLUtil
{
	public static void toXmlFile(Object object)
	{
		JFileChooser fileChooser = new JFileChooser();
		if (fileChooser.showSaveDialog(null) == JFileChooser.APPROVE_OPTION)
		{
			String fileName = fileChooser.getSelectedFile().getAbsolutePath();
			if (!fileName.endsWith(".xml"))
			{
				fileName += ".xml";
			}
			
			try(BufferedWriter out = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(fileName), "UTF8"));)
			{
				toXmlStream(object, out);
			}
			catch (IOException e)
			{
				JOptionPane.showMessageDialog(null, e.getMessage());
			}
		}
	}
	
	public static void toXmlStream(Object object, Writer out)
	{
		XStream xstream = new XStream(new DomDriver("UTF-8", new NoNameCoder()));
		xstream.autodetectAnnotations(true);
		xstream.toXML(object, out);
	}

	public static String camelToUnderScore(String camel)
	{
		return camel;
	}
}
