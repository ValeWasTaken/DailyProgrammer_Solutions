# Objective:
# Create a calculator of some sort.
# Extra credit: Program multiple functions (Ex: Find F=M*A, A=F/M, and M=F/A)
#

def main():
        print("Movie cost calculator\n"
                "Please enter your information to find the cost: ")
        total = 0.00
        ticketCost = 8.50
        tickets = input("How many tickets would you like to purchase? ")
        total += (tickets * ticketCost)

        snacks = raw_input("Would you like to purchase any snacks? (Y/N): ")
        snacks = snacks.lower()

        if(snacks.startswith('n'):
                total *= 1.07 # Assumes tax rate of 7%
                print("Very well, your total is $"+str(total)+" enjoy the movie!")
                exit()
        elif(snacks.startswith('y'):
                print("Excellent choice! Here is our menu: \n"
                        "1. Popcorn -- $4.50\n"
                        "2. Soda    -- $2.25\n"
                        "3. Combo   -- $5.75\n")
                snackChoice = raw_input("Which selection would you like to order? ")
                if(snackChoice == '1'):
                        total = (total + 4.50) * 1.07
                        print("Enjoy your popcorn and movie! Your total will be: $"+str(total))
                        exit()
                elif(snackChoice == '2'):
                        total = (total + 2.25) * 1.07
                        print("Enjoy your soda and movie! Your total will be: $"+str(total))
                        exit()
                elif(snackChoice == '3'):
                        total = (total + 5.75) * 1.07
                        print("Enjoy your combo and movie! Your total will be: $"+str(total))
                        exit()
                else:
                        print("Invalid input. Restarting program.")
                        main()
        return 0
main()

# Note: Since this was a very basic program I didn't bother making it very long.
# Naturally if one really needed a movie program like this they would add different ticket prices for
# students, seniors, adults, veterans, children, etc.. They would have options for buying multiple
# snacks and more options on things to buy. In other words there would be a lot else needed but this is just a
# proof of concept to show I understand enough to do the rest if I felt inclined to.
