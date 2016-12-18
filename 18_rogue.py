def generate_new_row(prev_row, cnt):
    new_row = ""
    for x in range(len(prev_row)):
        if x == 0 and (prev_row[x:x+2] == '^.' or prev_row[x:x+2] == '..'):
            new_row += '.'
            cnt += 1
        elif x == len(prev_row)-1 and (prev_row[x-1:x+1] == '.^' or prev_row[x-1:x+1] == '..'):
            new_row += '.'
            cnt += 1
        elif prev_row[x-1:x+2] == '^^^' or prev_row[x-1:x+2] == '.^.' or prev_row[x-1:x+2] == '...' or prev_row[x-1:x+2] == '^.^':
            new_row += '.'
            cnt += 1
        else:
            new_row += '^'
    return new_row, cnt


def solve(first_line, max_rows = 40):
    first_line.strip()
    solution = [first_line]
    cnt = first_line.count('.')
    while len(solution) < max_rows:
        new_row, cnt = generate_new_row(solution[-1], cnt)
        solution.append(new_row)
    return cnt, solution

if __name__ == '__main__':
    cnt, sol = solve(open('data/18_rogue.data').readline(),400000)
    print('Number of safe tiles is {0}'.format(cnt))