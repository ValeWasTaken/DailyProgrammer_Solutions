def main():
        text = raw_input("Enter text to disemvowel: ").replace(" ","")
        print ''.join(letter for letter in text if letter not in 'aeiouAEIOU')
        print ''.join(letter for letter in text if letter in 'aeiouAEIOU')
main()
