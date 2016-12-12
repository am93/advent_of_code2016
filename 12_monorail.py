from collections import defaultdict


def read_commands(file):
    return [line.strip().split(' ') for line in file]


def execute_command(cmd, registers, ptr):
    if cmd[0] == 'cpy':
        if cmd[1].isnumeric():
            registers[cmd[2]] = int(cmd[1])
        else:
            registers[cmd[2]] = registers[cmd[1]]
        ptr += 1
    elif cmd[0] == 'inc':
        registers[cmd[1]] += 1
        ptr += 1
    elif cmd[0] == 'dec':
        registers[cmd[1]] -= 1
        ptr += 1
    elif cmd[0] == 'jnz':
        if (cmd[1].isnumeric() and cmd[1] != 0) or (not cmd[1].isnumeric() and registers[cmd[1]] != 0):
            ptr += int(cmd[2])
        else:
            ptr += 1
    return ptr


def execute(filename, reg, second_part):
    registers = defaultdict(int)
    if second_part: registers['c'] = 1
    commands = read_commands(open(filename))
    ptr = 0
    while ptr < len(commands):
        ptr = execute_command(commands[ptr],registers,ptr)
    print('Value of register {0} is {1}.'.format(reg, registers[reg]))

if __name__ == '__main__':
    execute('data/12_monorail.data','a', True)