# Objective:
# Find the digital root of a number.
# Digital root example: 31337 -> 3+1+3+3+7 = 17 -> 1+7 = 8, the digital root.

def main():
    num = input("Enter number to find digital root of: ")
    while(num > 9):
        s = 0
        while(num > 0):
            s += (num % 10)
            num /= 10
        num = s
    print(num)
main()
