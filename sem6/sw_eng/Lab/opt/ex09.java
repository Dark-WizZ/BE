import org.openqa.selenium.By;
import org.openqa.selenium.firefox.*;
import org.openqa.selenium.*;

public class Main {
	public static void main(String[] args) {
		FirefoxDriver driver = new FirefoxDriver();
		driver.get("https://practicetestautomation.com/practice-test-login/");
		WebElement username = driver.findElement(By.id("username"));
		WebElement password = driver.findElement(By.id("password"));
		WebElement submit = driver.findElement(By.id("submit")); 
		username.sendKeys("student");
	    password.sendKeys("Password13");
	    submit.click();
	    String expectedUrl = "https://practicetestautomation.com/logged-in-successfully/";
	    String actualUrl = driver.getCurrentUrl();
	    if(actualUrl.equals(expectedUrl)) {
	    	System.out.println("Test passed");
	    }else {
	    	System.out.println("Test failed");
	    }
	}
}
