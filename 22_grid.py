def read_node_data(data):
    nodes = []
    for line in data:
        if not '/dev/grid' in line:
            continue
        splitted = line.split()
        nodes.append((int(splitted[2][:-1]), int(splitted[3][:-1])))
    return nodes


def solve(data):
    pairs = {}
    nodes = read_node_data(data)
    for i, n1 in enumerate(nodes):
        for j, n2 in enumerate(nodes):
            if i == j:
                continue
            if n1[0] <= n2[1] and n1[0] != 0:
                if not (j,i) in pairs.keys():
                    pairs[(i,j)] = 1

    return len(pairs.keys())


if __name__ == '__main__':
    print(solve(open('data/22_grid.data')))