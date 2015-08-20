import java.util.Scanner;

public class easy_challange_115 {
	private static Scanner userInput = new Scanner(System.in);
	
	public static void main(String[]args){
		int userGuess = 0;
		int correctNum = (int) (Math.random() * 1000);
		System.out.println("I'm thinking of a number between 1 and 999..");
		
		while(userGuess != correctNum)
		{
			System.out.println("Guess my number: ");
			System.out.println(correctNum);
			userGuess = userInput.nextInt();
			
			if(userGuess == correctNum){
				System.out.println("You win! You guessed my number!");
			} else if(userGuess < correctNum){
				System.out.println("Your guess was too low.");
			} else if(userGuess > correctNum) {
				System.out.println("Your guess was too high.");
			} else {
				System.out.println("Error.");
			}
		}
	}
}
