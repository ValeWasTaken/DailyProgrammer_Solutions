global braille_dictionary

braille_dictionary = {
'a': 'O.....',
'b': 'O.O...',
'c': 'OO....',
'd': 'OO.O..',
'e': 'O..O..',
'f': 'OOO...',
'g': 'OOOO..',
'h': 'O.OO..',
'i': '.OO...',
'j': '.OOO..',
'k': 'O...O.',
'l': 'O.O.O.',
'm': 'OO..O.',
'n': 'OO.OO.',
'o': 'O..OO.',
'p': 'OOO.O.',
'q': 'OOOOO.',
'r': 'O.OOO.',
's': '.OO.O.',
't': '.OOOO.',
'u': 'O...OO',
'v': 'O.O.OO',
'w': '.OOO.O',
'x': 'OO..OO',
'y': 'OO.OOO',
'z': 'O..OOO'
}

def convert_to_english_from_braille(input):
    reverse_dictionary = dict ((a,b) for b, a in braille_dictionary.items())
    message = ''
    print "\nYour messaged in English is..\n"
    fixed_input = input.upper()
    words = []
    for start in range(0, len(fixed_input), 6):
        words.append(fixed_input[start:(start + 6)])

    for word in words:
        message += "%s" % (reverse_dictionary[word])
    print message

def convert_to_braille_from_english(input):
    message = ''
    print "\nYour message in Binary is..\n"
    for letter in input:
        message += "%s" % (braille_dictionary[letter])
    print message

def restart():
    restart = raw_input("\nWould you like to do another conversion? (Y/N): ").upper()
    if(restart == 'Y'):
        main()
    elif(restart == 'N'):
        exit()
    else:
        print("Invalid entry, please try again.")
        restart()

def menu():
    phrase1 = "Type what you would like to convert into "
    print("\n- - - - - - - -- PROGRAM MENU -- - - - - - - -\n"
          "Please choose a desired conversion: \n"
          "1 ) Braille to English\n"
          "2 ) English to Braille\n"
          "3 ) No conversion, exit program.")
    user_choice = input("\n")
    
    if(user_choice == 1):
        user_input = raw_input(str(phrase1) + "English\n::\t")
        convert_to_english_from_braille(user_input)
    elif(user_choice == 2):
        user_input = raw_input(str(phrase1) + "Braille\n::\t")
        convert_to_braille_from_english(user_input)
    elif(user_choice == 3):
        exit()
    else:
        print("Invalid selection. Please try again.")
        main()
    

def main():
    menu()
    restart()
main()
