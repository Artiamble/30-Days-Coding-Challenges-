
//addition of 2 numbers using 2 variables
import java.util.Scanner;
public class Addition {

	public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
	System.out.println("First No...");
	int a=sc.nextInt();
	System.out.println("Second No...");
	int b=sc.nextInt();
	a+=b;
	System.out.println("Result : "+a);
	}

}
