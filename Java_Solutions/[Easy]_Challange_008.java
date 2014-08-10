public class [Easy]_Challange_008 {
	public static void main (String[]args)
	{
		int beerNum = 99;
		String word = "bottles";

		while (beerNum > 0)
		{
			if(beerNum == 1)
			{word = "bottle";} // Change wording if last bottle.

      			//All printed on one line for extra credit.
			System.out.print(beerNum + " " + word + " of beer on the wall! ");
			System.out.print(beerNum + " " + word + " of beer! ");
			System.out.print("Take one down, ");
			System.out.print("pass it around, ");
			beerNum--;
		}
		if(beerNum == 0)
		{System.out.println("No more bottles of beer on the wall");}
		
		else
		{System.out.println("Error.");}
	}
}
