# Disemvoweler
# Remove the vowels from words and output the message (without vowels)
# followed by the vowels (in order) on the next line.

def main():
        text = raw_input("Enter text to disemvowel: ").replace(" ","")
        print ''.join(letter for letter in text if letter not in 'aeiouAEIOU')
        print ''.join(letter for letter in text if letter in 'aeiouAEIOU')
main()

# Note: I originally made this program much differently but after seeing a post on Reddit
# using 'join' and 'replace' I redid my program to look more similar to their solution so I could learn more.
