//swapping of two numbers without using 3rd variable
import java.util.Scanner;

public class Swapping2 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Before Swapping...");
		System.out.println("===================");
		System.out.println("Enter First No...");
		int a=sc.nextInt();
		System.out.println("Enter Second No...");
		int b=sc.nextInt();
		a=a-b;
		b=a+b;
		a=b-a;
		System.out.println("After Swapping...");
		System.out.println("===================");
		System.out.println("First No : "+a);
		System.out.println("Second No : "+b);	
	}

}
