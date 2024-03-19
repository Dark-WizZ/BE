import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;

public class Main {
  
  public static void main(String[] args) {
     System.setProperty("webdriver.chrome.driver", "C:\\chromedriver\\chromedriver.exe");
     WebDriver driver = new ChromeDriver();
     
     driver.get("https://dark-wizz.github.io/odin-recipies/");
     driver.manage().window().maximize();
     
     // Find the <p> element on the page
     System.out.println("The number of <li> elements present are: " + driver.findElements(By.tagName("li")).size());
     
     driver.quit();
  }
}
