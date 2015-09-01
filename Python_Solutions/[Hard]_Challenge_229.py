def challenge_229(power):
    numbers = []
    for x in range(0, 10**power, 7):
        if x % 7 == 0 and int(str(x)[::-1]) % 7 == 0:
            numbers.append(x)
    print(sum(numbers))
    
challenge_229(3)
