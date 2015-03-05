package plugin.analyzer;

import java.lang.Exception;

/** AnalyzeException - special kind of exception that can be thrown by ModelAnalyzer */
public class AnalyzeException extends Exception
{
	private static final long serialVersionUID = 1L;

	public AnalyzeException(String msg)
	{
		super(msg);
	}
}
