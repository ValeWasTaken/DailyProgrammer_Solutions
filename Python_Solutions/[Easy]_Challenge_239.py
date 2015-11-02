def game_of_threes(n):
    while n != 1:
        if n % 3 == 0:
            n /= 3
        elif n % 3 == 1:
            n -= 1
        elif n % 3 == 2:
            n += 1
        print(n)
