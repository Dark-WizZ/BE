import java.util.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.*;


public class Main {
	public static void main(String[] args) {
		FirefoxDriver driver = new FirefoxDriver();
		driver.get("C:\\Users\\Akram\\Documents\\ex11.html");
		List<WebElement> elements = driver.findElements(By.tagName("input"));
		elements.get(0).sendKeys("235");
		elements.get(1).sendKeys("15");
		elements.get(2).click();
		String result = elements.get(3).getAttribute("value");
		System.out.println("The GCD is: "+result);
	}
}