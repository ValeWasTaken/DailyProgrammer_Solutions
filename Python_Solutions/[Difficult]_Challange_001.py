import math

def restart():
	restart = raw_input("Would you like to play again? (Y/N): ")
	restart = restart.upper()
	if(restart == 'Y'):
		numGuessed = False
		main()
	elif(restart == 'N'):
		exit()
	else:
		print("Invalid entry, please try again.")
		restart()

def main():
	print('Let\'s play a game!\n'
		'You pick a number 1-100 '
		'and I will try to guess your number!\n'
		'If I guess too low, type "higher" or "h"\n'
		'If I guess too high, type "lower" or "l"\n'
		'If I guess your number, type "correct" or "c"!\n')

	numGuessed = False
	minNum = 1
	maxNum = 100
	guess = 50	
	
	while(numGuessed != True):
		guess = int((maxNum + minNum)/2)
		userResponse = raw_input("Is your number: %d?\n" % guess)
		userResponse = userResponse.lower()		

		if(guess == 99):
			guess = 100
		elif(guess == 100):
			print("May I remind you the game only allowed numbers 1-100?\n")

		if(userResponse.startswith('c')):
			print("Woohoo! I got it!\n")
			numGuessed = True
			restart()
		elif(userResponse.startswith('h')):
			minNum = guess
		elif(userResponse.startswith('l')):
			maxNum = guess
		else:
			print("Error, incorrect input.")
main()
