# Objective:
# Take a number and find the sum of its digits.
# Ex: 123456 is 1+2+3+4+5+6
# Then find the sum of that number, and so forth, until you remain with one digit.
#

def main():
    sum = 0
    num = input("Enter a number: ")
    while (len(str(num)) > 1):
        for digit in str(num):
            sum += int(digit)
        num = sum
        sum = 0
    print(num)
main()
