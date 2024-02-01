import com.thoughtworks.selenium*;
@SuppressWarnings("deprecation")
public class objectcount extends SeleneseTestCase {
  public void setUp() throws Exception {
    setUp("http://www.google.com/","*firefox");
  }
  public void testloginlogout(){
    selenium.setSpeed("1000");
    selenium.open("/mail/help/intl/en/logout.html#hl=en");
    selenium.waitForPageToLoad("30000");
    selenium.windowMaximize();
    int num = selenium.getXpathCount("//p").intValue();
    System.out.println("The number of option elements present are " +num);
  }
}
