# Python 3.6.5
import codecs

option = input("Type 'e' to encode, 'd' to deocde to rot-13.\n")
if option == 'e':
    text = input('Enter plaintext to encode: ')
    print(codecs.encode(text, 'rot-13'))
elif option == 'd':
    text = input('Enter plaintext to decode: ')
    print(codecs.decode(text, 'rot-13'))
else:
    print('Invalid option.')
