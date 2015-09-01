def challenge_229(power):
    sum = 0
    for x in range(0, 10**power, 7):
        if int(str(x)[::-1]) % 7 == 0:
            sum += x
    print(sum)
    
challenge_229(3)
