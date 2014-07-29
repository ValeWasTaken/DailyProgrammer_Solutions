def restart():
    restart = raw_input("Would you like to play again? (Y/N) ")
    restart = restart.upper()
    if(restart == 'Y'):
        game()
    elif(restart == 'N'):
        exit()
    else:
        print("Invalid input.")
        restart()

def lose():
    gameOver = True
    print("You lose! You get NOTHING! -- Game over.")
    restart()

def win():
    gameOver = True
    print("You win! Congratsulations!")
    restart()

def game():
    gameOver = False
    
    print("You wake up disorientated and lying in a field..\n"
          "Your controls are: \n"
          "n : Go North\n"
          "e : Go East\n"
          "s : Go South\n"
          "w : Go West\n"
          "i : Inspect surrounding\n"
          "d : Damn it all! (Suicide)\n")
    while(gameOver == False):
        userAction = raw_input("What will you do? ")
        userAction = userAction.lower()

        if(userAction == 'n' or userAction == 'e' or userAction == 's' or userAction == 'w'):
            print("You fool! You didn't check your surrounding better,\n"
                  "this field was just a small circle over a 5000ft drop!\n")
            lose()
        elif(userAction == 'i'):
            print("A quick look around tells you that this field is actually over a "
                  "5000ft drop!\nGood thing you looked around.\n")
        elif(userAction == 'd'):
            print("You figured out it was all a dream! You kill your dream self and wake up safely.\n")
            win()
        else:
            print("Invalid command. Please try again. ")
    return 0
game()
