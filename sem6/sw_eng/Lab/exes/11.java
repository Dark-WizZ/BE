import com.thoughtworks.selenium.*;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
@SuppressWarnings("deprecation")
public class GcdTest extends SeleneseTestCase{
@Before
public void setUp() throws Exception {
selenium = new DefaultSelenium("localhost", 4444, "*chrome",
"file:\\\C:\\Users\\nehru\\Desktop\\GCD.html");
selenium.start();
}
@Test
public void testGcd() throws Exception {
selenium.setSpeed("2000");
selenium.open("file:\\\C:\\Users\\nehru\\Desktop\\GCD.html");
selenium.windowMaximize();
selenium.type("name=n1", "5");
selenium.type("name=n2", "6");
selenium.click("css=input[type=\"button\"]");
String result = selenium.getValue("name=result");
System.out.println("the gcd is : "+result);
}
@After
public void tearDown() throws Exception {
selenium.stop();
}
}
