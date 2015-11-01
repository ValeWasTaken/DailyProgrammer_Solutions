import random

def test():
    data = input()
    answer = ''
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    for char in data:
        if char == 'c':
            answer += random.choice(consonants)
        elif char == 'C':
            answer += random.choice(consonants).upper()
        elif char == 'v':
            answer += random.choice(vowels)
        elif char == 'V':
            answer += random.choice(vowels).upper()
        else:
            answer += char
    print(answer)
test()
