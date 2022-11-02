from random import randint
from time import time

def generate_bracket(opens):
    if opens == 0:
        return ''
    s = '('
    o = 1
    c = 0
    i = 0
    while o < opens:
        r = randint(0, 1)
        if r and not c >= o:
            s += ')'
            c += 1
        else:
            s += '('
            o += 1
    if not o == c:
        s += ')' * (o-c)
    return s

# Do testowania
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

opens = 0
start = time()

for i in range(1000):
    for _ in range(10):
        bracket = generate_bracket(i)
        for j in bracket:
            if j == '(':
                opens += 1
        if opens != i:
            print(f'Error at:\n   Bracket: {bracket}\n    Valid: {bracket_validation(bracket)}\n    Expected: {i}\n    Found: {opens}')
        opens = 0
else:
    print(f'Done. Took {time() - start}s. No issues found.')