import java.util.Scanner;
public class StringReverse {
         public static void main(String[] args) {
	 String s;
	 Scanner sc=new Scanner(System.in);
	 System.out.print("Enter String...");
	 s=sc.nextLine();
	 System.out.print("After Reverse String is...");
	 int i=s.length();
	 while(i>0) {
          System.out.print(s.charAt(i-1));
          i--;		 
	 }
	}
       }
