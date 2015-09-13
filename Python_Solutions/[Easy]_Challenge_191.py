# Python 3.4
from collections import Counter

f = open('pg47498.txt', 'r')
answer = Counter(f.read().split())
print(answer)
