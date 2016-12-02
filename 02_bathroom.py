from collections import defaultdict

def generate_keypad(size=3):
    """
    Function generates simple 3x3 "keypad" implemented as defaultdict
    """
    keypad = defaultdict(int)
    for x in range(size):
        for y in range(size):
            keypad[(x,y)] = str(x + y*3 + 1)
    return keypad


def generate_new_keypad(filename):
    """
    Function generates special keypad from text file (given by advent of code 2016 - task 2)
    """
    keypad = defaultdict(int)
    x = 0
    y = 0
    with open(filename) as f:
        for line in f:
            for c in line.strip().split(','):
                keypad[(x,y)] = c
                x +=1
            x = 0
            y += 1
    return keypad


def move_pointer(c,x,y,keypad,size=3):
    """
    Simple movement on classic 3x3 keypad
    """
    if c == 'U':
        return x, max(0, y-1)
    if c == 'D':
        return x, min(size-1, y+1)
    if c == 'R':
        return min(size-1, x+1), y
    if c == 'L':
        return max(0, x-1), y


def move_pointer_advanced(c,x,y,keypad, size=5):
    """
    Implementation of movement on more advanced keypad (second part of task)
    """
    if c == 'U':
        if y-1 > -1 and keypad[(x,y-1)] != 'x': return x, max(0, y-1)
        else: return x,y
    if c == 'D':
        if y+1 < size and keypad[(x, y+1)] != 'x': return x, min(size-1, y+1)
        else: return x,y
    if c == 'R':
        if x+1 < size and keypad[(x+1, y)] != 'x': return min(size-1, x+1), y
        else: return x,y
    if c == 'L':
        if x-1 > -1 and keypad[(x-1, y)] != 'x': return max(0, x-1), y
        else: return x,y


def solve_code(filename, x, y, keypad, pointer_move):
    f = open(filename)
    code = ""
    for line in f:
        for c in line.strip():
            x,y = pointer_move(c,x,y,keypad)
        code += str(keypad[(x,y)])
    return code

if __name__ == '__main__':
    keypad = generate_new_keypad('data/02_keypad2.data')
    code = solve_code('data/02_bathroom.data', 0, 2, keypad, move_pointer_advanced)
    print('Bathroom code is {0}'.format(code))