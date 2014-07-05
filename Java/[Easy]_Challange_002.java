import java.util.Scanner;

public class Easy_Challange_002
{
	private static Scanner userInput;

	public static void main(String args[])
	{	
		String menuChoice;
		double a,f,m;
		userInput = new Scanner(System.in);
		
		System.out.println("What would you like to find?\n"
				+"Options: \nA - Acceleration\nF - Force\nM - Mass\n");
		menuChoice = userInput.nextLine();
		
		if(menuChoice.equalsIgnoreCase("A"))
		{
			// A = F/M
			System.out.println("Please enter the force: ");
			f = userInput.nextDouble();
			System.out.println("Please enter the mass: ");
			m = userInput.nextDouble();
			
			a = (f/m);
			System.out.println("The acceleration is: " + a);
		}
		
		else if(menuChoice.equalsIgnoreCase("F"))
		{
			// F = M*A
			System.out.println("Please enter the mass: ");
			m = userInput.nextDouble();
			System.out.println("Please enter the acceleration: ");
			a = userInput.nextDouble();
			
			f = (m*a);
			System.out.println("The acceleration is: " + f);
		}
		
		else if(menuChoice.equalsIgnoreCase("M"))
		{
			// M = F/A
			System.out.println("Please enter the force: ");
			f = userInput.nextDouble();
			System.out.println("Please enter the acceleration: ");
			a = userInput.nextDouble();
			
			m = (f/a);
			System.out.println("The acceleration is: " + m);
		}
		
		else 
		{
		System.out.println("Error. Please restart the program and try again.");	
		}
	}
}
