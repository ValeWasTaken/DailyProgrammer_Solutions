# Objective:
# Create a random password generator with the following attributes:
# User determines how many passwords generated & user specifies length of password.
#
from random import randint

def main():
        numOfPasswords = input("How many passwords would you like to generate? ")
        passLength = input("How long would you like your password(s) to be? ")
        selection = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        result = ''
        for a in range(numOfPasswords):
                for b in range(passLength):
                        place = randint(0, len(selection) -1)
                        result += selection[place]
                print(result)
                result = ''
main()
