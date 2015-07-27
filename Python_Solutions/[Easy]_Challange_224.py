# Python 3.4
# Shuffles a user inputted list. Ex: '1 2 3 4' may turn into '3 2 4 1' or any other permutation.
import random

def shuffle(string):
    default_string = string.split()
    shuffled_string = []
    while len(shuffled_string) < len(string.split()):
        random_item = default_string.pop(random.randint(0, len(default_string)-1))
        shuffled_string.append(random_item)
    print(shuffled_string)
shuffle(input())
