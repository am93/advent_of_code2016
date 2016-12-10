from collections import defaultdict
from functools import reduce

def read_commands(f):
    commands = []
    bots = defaultdict(list)
    for row in f:
        splitted = row.strip().split(' ')
        if splitted[0] == 'value':
            if splitted[-1] in bots.keys():
                bots[splitted[-1]].append(int(splitted[1]))
                bots[splitted[-1]].sort()
            else:
                bots[splitted[-1]] = [int(splitted[1])]
        else:
            commands.append([int(splitted[1]), int(splitted[6]), splitted[5], int(splitted[-1]), splitted[-2]])

    return bots, commands


def check_bots(bots):
    for key, value in bots.items():
        if value == [17,61]: print('Bot {0} has {1}'.format(key, value))


def execute_commands(bots, commands):
    outputs = defaultdict(list)
    idx = 0
    while len(commands) > 0:
        cmd = commands[idx]
        if len(bots[str(cmd[0])]) == 2 and (cmd[2] == 'output' or len(bots[str(cmd[1])]) < 2) and (cmd[4] == 'output' or len(bots[str(cmd[3])]) < 2):
            tmp = bots[str(cmd[0])]
            bots[str(cmd[0])] = []
            if cmd[2] == 'bot':
                bots[str(cmd[1])].append(tmp[0])
                bots[str(cmd[1])].sort()
            else:
                outputs[str(cmd[1])].append(tmp[0])
            if cmd[4] == 'bot':
                bots[str(cmd[3])].append(tmp[1])
                bots[str(cmd[3])].sort()
            else:
                outputs[str(cmd[3])].append(tmp[1])

            commands.pop(idx)
            idx = 0
            check_bots(bots)
            continue
        idx += 1
        if idx > len(commands):
            print('Error ! Can\'t execute all commands !')
            return None, None

    return bots, outputs

if __name__ == '__main__':
    bots, commands = read_commands(open('data/10_bots.data'))
    check_bots(bots)
    bots, outputs = execute_commands(bots, commands)
    print('Result for second part is : {0}'.format(reduce(lambda x,y: x*y,[outputs[str(x)][0] for x in range(3)],1)))
