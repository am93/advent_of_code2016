def solve(compressed, second=False):
    result = 0

    if '(' not in compressed:
        return len(compressed)
    while '(' in compressed:
        result += compressed.find('(')
        compressed = compressed[compressed.find('('):]
        marker = compressed[1:compressed.find(')')].split('x')
        compressed = compressed[compressed.find(')') + 1:]
        if second:
            result += solve(compressed[:int(marker[0])], True) * int(marker[1])
        else:
            result += len(compressed[:int(marker[0])]) * int(marker[1])
        compressed = compressed[int(marker[0]):]

    result += len(compressed)
    return result

if __name__ == '__main__':
    compressed = open('data/09_dummy.data').read().strip()
    #print('First part result is {0}'.format(solve(compressed)))
    print('Second part result is {0}'.format(solve(compressed, True)))