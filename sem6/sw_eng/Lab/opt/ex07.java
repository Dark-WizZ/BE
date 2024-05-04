import org.openqa.selenium.*;
import java.util.*;
import org.openqa.selenium.firefox.*;
public class Main {
  public static void main(String[] args) {
	FirefoxDriver driver = new FirefoxDriver();
    driver.get("C:\\Users\\Akram\\Documents\\ex07.html");
    List<WebElement> checkboxes =
    		driver.findElements(By.xpath("//input[@type='checkbox']"));
    System.out.println("Number of checkboxes: "+
    		checkboxes.size());
    checkboxes.get(0).click();
    int checked = 0, unChecked = 0;
    for(int i=0; i<checkboxes.size(); i++) {
    	System.out.println(i+" checkbox is selected: "+checkboxes.get(i).isSelected());
    	if (checkboxes.get(i).isSelected()) {
    		checked++; 
    	}else {
    		unChecked++;
    	}
    }
    System.out.println("number of selected checkbox: "+checked);
    System.out.println("number of unselected checkbox: "+unChecked);
  }
}
