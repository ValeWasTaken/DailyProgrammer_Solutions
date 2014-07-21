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

def convert_to_braille_from_english(input):
    message = ''
    print "\nYour message in Binary is..\n"
    for letter in input:
        message += "%s" % (braille_dictionary[letter])
    print message

def restart():
    restart = raw_input("\nWould you like to do another conversion? (Y/N): ")
    restart = restart.upper()
    if(restart == 'Y'):
        main()
    elif(restart == 'N'):
        exit()
    else:
        print("Invalid entry, please try again.")
        restart()

def main():
    print("Type what you would like to convert into English\n")
    user_input = raw_input("\n")
    convert_to_braille_from_english(user_input)
    restart()
main()
