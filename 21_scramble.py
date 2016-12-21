from itertools import *

def scramble_inverse(goal):
    for p in permutations(goal):
        p = list(p)
        if solve(p, open('data/21_scramble.data')) == "".join(goal):
            return "".join(p)

def rotate_right(arr, n):
    return arr[-n:] + arr[:-n]


def rotate_left(arr, n):
    return arr[n:] + arr[:n]


def solve(scrm, instr):
    for line in instr:
        splitted = line.strip().split()
        nums = [int(x) for x in splitted if x.isdigit()]
        if line.startswith('swap position'):
            x,y = nums
            scrm[x], scrm[y] = scrm[y], scrm[x]
        elif line.startswith('swap letter'):
            x,y = splitted[2], splitted[-1]
            i,j  = scrm.index(x), scrm.index(y)
            scrm[i], scrm[j] = scrm[j], scrm[i]
        elif line.startswith('rotate left'):
            n = nums[0]
            scrm = rotate_left(scrm, n)
        elif line.startswith('rotate right'):
            n = nums[0]
            scrm = rotate_right(scrm, n)
        elif line.startswith('rotate based'):
            x = splitted[-1]
            n = scrm.index(x)
            n += (n >= 4) + 1
            scrm = rotate_right(scrm, n%len(scrm))
        elif line.startswith('reverse'):
            x,y = nums
            scrm[x:y+1] = scrm[x:y+1][::-1]
        else:
            x,y = nums
            z = scrm.pop(x)
            scrm = scrm[:y] + [z] + scrm[y:]
    return "".join(scrm)

if __name__ == '__main__':
    #print(solve(list('abcdefgh'),open('data/21_scramble.data')))
    print(scramble_inverse(list('fbgdceah')))