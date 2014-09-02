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
