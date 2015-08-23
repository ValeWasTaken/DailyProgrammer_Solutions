import random

def main():
    print("Welcome to guess-that-number game!\n"
          +"If at any point you would like to quit, please type 'exit'.\n\n"
          +"I have thought of a number, 1-100, see if you can guess it!")
    number = random.randrange(1,101)
    guess = 0

    while(guess != number):
        guess = raw_input("Guess a number: ").lower()
        
        if(guess == "exit"):
            exit()

        if(int(guess) == number):
            print("You guessed it! You win!")
            exit()
        elif(int(guess) > number):
            print("Your number is too high!")
        elif(int(guess) < number):
            print("Your number is too low!")
        else:
            print("Error.")        
main()
