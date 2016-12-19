import operator

import math


def solve(num=5):
    elves = [1] * num
    idx1 = 0
    idx2 = 1
    while True:
        if idx1 == idx2: break
        if elves[idx2] > 0:
            elves[idx1] += elves[idx2]
            elves[idx2] = 0
            idx1 = (idx2 + 1) % num
            while elves[idx1] == 0:
                idx1 = (idx1 + 1) % num
            idx2 = (idx1 + 1) % num
        else:
            idx2 = (idx2 +1) % num
    idx, val = max(enumerate(elves), key=operator.itemgetter(1))
    return idx


def solve_second(num=5):
    elves = [(i+1,1) for i in range(num)]
    idx1 = 0
    idx2 = math.floor(num/2)
    while True:
        if idx1 == idx2: break
        if elves[idx2][1] > 0:
            elves[idx1] = (elves[idx1][0], elves[idx1][1] + elves[idx2][1])
            elves.pop(idx2)
            if idx1 + 1 >= len(elves):
                idx1 = 0
            else:
                idx1 += 1
            while elves[idx1][1] == 0:
                idx1 = (idx1 + 1) % elves
            idx2 = math.floor(idx1 + len(elves)/2) % len(elves)
        else:
            idx2 = (idx2 + 1) % num
        if len(elves) % 10000 == 0:
            print(len(elves))
    return elves[0]

if __name__ == '__main__':
    #print(solve(3001330))
    print(solve_second(3001330))