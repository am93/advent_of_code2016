def generate_data(start, length):
    data = start
    while len(data) < length:
        tmp = data[::-1].replace('1','2').replace('0','1').replace('2','0')
        data += '0'+tmp
    return data[0:length]


def calculate_checksum(data):
    chck = "".join([str(int(data[i] == data[i+1])) for i in range(0,len(data)-1,2)])
    if len(chck) %2 == 1:
        return chck
    else:
        return calculate_checksum(chck)


def solve(start, length):
    data = generate_data(start, length)
    checksum = calculate_checksum(data)
    return checksum

if __name__ == '__main__':
    print(solve('10001110011110000',35651584))