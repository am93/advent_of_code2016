from collections import Counter
import operator


def solve(filename, second=False):
    result = 0
    with open(filename) as f:
        for line in f:
            room = "".join(sorted(line.split('-')[:-1]))
            number = int(line.split('-')[-1].split('[')[0])
            checksum = line.split('-')[-1].split('[')[1].rstrip('\n').rstrip(']')
            analysis = sorted([(key, -val) for key, val in Counter(room).items()], key=operator.itemgetter(1, 0))[0:5]
            if "".join([x for (x,_) in analysis]) == checksum:
                result += number
                decrypted = "".join([chr((((ord(x) - 97) + int(number)) % 26) + 97) for x in room])
                if 'northpole' in decrypted and second : return number
    return result

if __name__ == '__main__':
    print(solve('data/04_security.data', second=True))