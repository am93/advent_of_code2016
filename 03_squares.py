from functools import reduce
import operator

def read_data(file):
    for line in file:
        yield list(map(int, line.split()))


def read_data_advanced(file):
    count = 0
    tmp = []
    for line in file:
        tmp.append(list(map(int, line.split())))
        count += 1
        if count == 3:
            for i in range(count):
                yield [x for x in map(operator.itemgetter(i), tmp)]
            count = 0
            tmp = []


def test_triangle(acc,list):
    return acc + int(all([list[x%3] + list[(x+1)%3] > list[(x+2)%3] for x in range(3)]))


def count_three_sided_squares(file):
    return reduce(test_triangle,read_data_advanced(file),0)

if __name__ == '__main__':
    f = open('data/03_squares.data')
    print("There are {0} valid triangles.".format(count_three_sided_squares(f)))
    f.close()