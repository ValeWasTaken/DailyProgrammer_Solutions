#include <stdio.h>

#define TRUE    1
#define FALSE   0

main()
{
        int Alive = TRUE;
        int choice;
        printf("\033[2J\033[1;1H"); // Clear screen
        printf("You wake up disorientated, lying in a field..\n");
        printf("Your controls are: \n"
                "n : Go North\n"
                "e : Go East\n"
                "s : Go South\n"
                "w : Go West\n"
                "i : Inspect surrounding\n"
                "d : Damn it all! (Suicide)\n");

        while(Alive == TRUE)
        {
                printf("What will you do? ");
                choice = getchar();

                if(choice == '\n'){ choice = getchar(); }

                if(choice == 'n' || choice == 'e' || choice == 's' || choice == 'w'){
                        printf("You fool! You didn't check your surrounding better,\n"
                                "this field was just a small circle over a 5000ft drop!\n");
                        printf("You lose!\n");
                        Alive = FALSE;}
                else if(choice == 'i'){
                        printf("A quick look around tells you that this field is actually over a "
                                "5000ft drop!\nGood thing you looked around.\n");}
                else if(choice == 'd'){
                        printf("You figured out it was all a dream! You kill your dream self and wake up.\n");
                        printf("You win!\n");
                        Alive = FALSE;}
                else {
                        printf("Invalid command. Please try again: ");
                }
        }
        return 0;
}
