from cmath import nan
from random import randint

def bracket_validation(s):
    c = 0
    for char in s:
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
        elif char == '\n':
            continue
        else:
            return False
    
    if c == 0:
        return True
    return False

def bracket_deepness(s):
    if not bracket_validation(s):
        return nan
    c = 0
    mc = 0
    for char in s:
        if char == '(':
            c += 1
            if c > mc:
                mc = c
        elif char == ')':
            c -= 1
    return mc

def generate_bracket(deepness):
    s = '('
    i = 0
    while i < deepness - 1:
        r = randint(0,1)
        if r == 0:
            i += 1
            s += '('
        if r == 1:
            i -= 1
            s += ')'
    c = 0
    for char in s:
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
    s += ')' * c
    return s

for n in range(1, 1000):
    b = generate_bracket(5)
    if len(b) > 500:
        continue
    if not bracket_validation(b) or not bracket_deepness(b) == 5:
        print(f'Error at {n}:\n    {b}\n    Valid: {bracket_validation(b)}\n    Deepness: {bracket_deepness(b)}')
        break
else: 
    print('No issues found.')