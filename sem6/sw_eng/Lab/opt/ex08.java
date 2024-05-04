import org.openqa.selenium.*;
import java.util.*;
import org.openqa.selenium.firefox.*;
public class Main {
  public static void main(String[] args) {
	FirefoxDriver driver = new FirefoxDriver();
	driver.get("https://www.google.com/");
	List<WebElement> count = driver.findElements(By.tagName("div"));
	System.out.println("The number of <div> elements present = " 
	  + count.size());
  }
}
