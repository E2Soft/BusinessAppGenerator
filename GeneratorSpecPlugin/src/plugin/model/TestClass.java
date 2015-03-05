package plugin.model;

public class TestClass
{
	String id;
	int a;
	int b;
	int c;
	String d;
	TestClassSecond second;

	TestClassThird third;
	public TestClass(String id, int a, int b, int c, String d, TestClassSecond second, TestClassThird third)
	{
		this.id = id;
		this.a = a;
		this.b = b;
		this.c = c;
		this.d = d;
		this.second = second;
		this.third = third;
	}
}
