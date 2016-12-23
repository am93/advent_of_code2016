from collections import defaultdict


def read_commands(file):
    return [line.strip().split(' ') for line in file]


def execute_command(cmd, registers, ptr, cmds):
    if cmd[0] == 'cpy':
        if cmd[1].lstrip('-').isnumeric() and cmd[2].lstrip('-').isnumeric():
            return ptr + 1, cmds
        if cmd[1].lstrip('-').isnumeric():
            registers[cmd[2]] = int(cmd[1])
        else:
            registers[cmd[2]] = registers[cmd[1]]
        ptr += 1
    elif cmd[0] == 'inc':
        if cmd[1].lstrip('-').isnumeric():
            return ptr + 1, cmds
        registers[cmd[1]] += 1
        ptr += 1
    elif cmd[0] == 'dec':
        if cmd[1].lstrip('-').isnumeric():
            return ptr + 1, cmds
        registers[cmd[1]] -= 1
        ptr += 1
    elif cmd[0] == 'jnz':
        if (cmd[1].lstrip('-').isnumeric() and cmd[1] != 0) or (not cmd[1].lstrip('-').isnumeric() and registers[cmd[1]] != 0):
            if cmd[2].lstrip('-').isnumeric():
                ptr += int(cmd[2])
            else:
                ptr += registers[cmd[2]]
        else:
            ptr += 1
    elif cmd[0] == 'tgl':
        if not cmd[1].lstrip('-').isnumeric():
            x = registers[cmd[1]]
        else:
            x = int(cmd[1])

        if ptr + x >= len(cmds): return ptr +1, cmds
        if cmds[ptr+x][0] == 'inc': cmds[ptr+x][0] = 'dec'
        elif cmds[ptr+x][0] == 'dec': cmds[ptr+x][0] = 'inc'
        elif cmds[ptr+x][0] == 'jnz': cmds[ptr+x][0] = 'cpy'
        elif cmds[ptr+x][0] == 'cpy': cmds[ptr+x][0] = 'jnz'
        elif cmds[ptr+x][0] == 'tgl': cmds[ptr+x][0] = 'inc'
        ptr += 1

    return ptr, cmds


def execute(filename, reg, second_part):
    registers = defaultdict(int)
    registers['a'] = 12
    if second_part: registers['c'] = 1
    commands = read_commands(open(filename))
    ptr = 0
    while ptr < len(commands):
        ptr, commands = execute_command(commands[ptr], registers, ptr, commands)
        #print("--",ptr)
    print('Value of register {0} is {1}.'.format(reg, registers[reg]))

if __name__ == '__main__':
    execute('data/23_safe.data','a', False)