import re
import numpy as np


def display(screen):
    print('\n'.join(''.join('8' if pixel else ' '  for pixel in row) for row in screen))


def solve(width, height, data):
    screen = np.zeros((height, width), dtype=bool)
    for line in data:
        p = re.split(r'[ =]', line)
        if p[0] == 'rect':
            w, h = map(int, p[1].split('x'))
            screen[:h, :w] = True
        elif p[0] == 'rotate':
            if p[1] == 'row':
                y, n = int(p[3]), int(p[5])
                screen[y] = np.roll(screen[y], n)
            else:
                x, n = int(p[3]), int(p[5])
                screen[:,x] = np.roll(screen[:,x], n)
    return screen

answer = solve(50, 6, open('data/08_2fa.data'))
print('Number of active pixels is {0}.'.format(np.sum(answer)))
print('Display:')
display(answer)