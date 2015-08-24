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
