def check_firewall(ip, firewall):
    for begin, end in firewall:
        if begin <= ip <= end:
            return False
    if ip < 2 ** 32: return True
    return False


def solve(input_file):
    firewall = sorted([list(map(int,line.strip().split('-'))) for line in input_file])
    candidates = [x[1] + 1 for x in firewall]
    valid = [c for c in candidates if check_firewall(c, firewall)]

    total = 0
    for ip in valid:
        while check_firewall(ip, firewall):
            total += 1
            ip += 1

    print("Lowest allowed IP addres is {0}.".format(valid[0]))
    print("Number of all allowed IPs is {0}.".format(total))

if __name__ == '__main__':
    solve(open('data/20_firewall.data'))