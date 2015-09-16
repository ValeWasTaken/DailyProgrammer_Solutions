# Python 3.4
def is_palindrome(lines):
    s = ''
    for line in range(lines):
        for letter in input():
            if letter.isalpha():
                s += letter.lower()

    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
is_palindrome(int(input()))
