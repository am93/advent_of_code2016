from collections import defaultdict


def parse_input(filename):
    result = []
    with open(filename) as f:
        for line in f:
            result += line.split(', ')

    return result


def move(data, part1=False):
    m = (0, 1)
    x,y = 0,0
    seen = defaultdict(int)
    for entry in data:
        m = (m[1], -m[0]) if entry[0] == "R" else (-m[1], m[0])
        val = int(entry[1:])
        for _ in range(val):
            x += m[0]
            y += m[1]
            if seen[(x,y)] > 0 and not part1: return (x,y)
            seen[(x,y)] = 1

if __name__ == '__main__':
    data = parse_input('data/01_taxicab.data')
    end = move(data)
    print('Bunny HQ at ({0},{1})'.format(end[0],end[1]))
    print('You are {0} blocks away'.format(abs(end[0])+abs(end[1])))