# Python 3.4
def check_order(word):
    temp = ' '
    orientation = 0
    for char in word:
        if ord(char) >= ord(temp):
            orientation += 1
        elif ord(char) <= ord(char):
            orientation -= 1
        temp = char
    if orientation == len(word):
        print('{0} IN ORDER'.format(word))
    elif orientation == -len(word):
        print('{0} REVERSE ORDER'.format(word))
    else:
        print('{0} NOT IN ORDER'.format(word))
