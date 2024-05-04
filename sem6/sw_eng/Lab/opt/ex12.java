import java.io.*;
import jxl.*;
import jxl.write.*;
import jxl.write.Number;
import jxl.write.biff.RowsExceededException;
import jxl.read.biff.BiffException;
import java.awt.Desktop;

public class Main{
	public static void main(String[] args) throws IOException,
	RowsExceededException,WriteException{
		String fileLoc = "C:\\Users\\Akram\\Documents\\student.xls";
		File inputWorkbook = new File(fileLoc);
		try {
			Workbook wb = Workbook.getWorkbook(inputWorkbook);
			WritableWorkbook writableWb = Workbook.createWorkbook(inputWorkbook, wb);
			WritableSheet sheet = writableWb.getSheet(0);
			for(int j=0; j<sheet.getRows(); j++) {
				for(int i=0; i<sheet.getColumns(); i++) {
					WritableCell cell = sheet.getWritableCell(i, j);
					if(cell.getType() == CellType.NUMBER) {
						Integer update = Integer.parseInt(cell.getContents()) - 10;
						update = update<0? 0 : update;
						Number n = new Number(i,j,update);
						sheet.addCell(n);
					}
				}
			}
			writableWb.write();
			writableWb.close();
			System.out.print("Opening the upadted file...");
			Desktop.getDesktop().open(inputWorkbook);
		}catch(BiffException e) {
			e.printStackTrace();
		}
	}
}