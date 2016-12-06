from collections import defaultdict
import operator


def solve(filename, size=6, func=max):
    analysis = [defaultdict(int) for _ in range(size)]
    with open(filename) as f:
        for line in f:
            for i, c in enumerate(line.strip()):
                analysis[i][c] += 1

    return "".join([func(a.items(), key=operator.itemgetter(1))[0] for a in analysis])

if __name__ == '__main__':
    word = solve('data/06_signal.data', size=8,func=min)
    print("Transmitted word is {0}.".format(word))