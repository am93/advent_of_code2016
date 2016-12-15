def parse_date(file):
    discs = []
    for line in file:
        splitted = line.strip().split(' ')
        discs += [[int(splitted[-1].rstrip('.')), int(splitted[3])]]
    return discs


def test_solution(discs, start):
    return all([(c[0] + x) % c[1] == 0 for x,c in zip(range(start+1, start+len(discs) + 1), discs)])


def solve(discs):
    count = -1
    solved = False
    while not solved:
        count += 1
        solved = test_solution(discs, count)
    return count

if __name__ == '__main__':
    discs = parse_date(open('data/15_discs.data'))
    print(solve(discs))