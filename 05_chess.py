import hashlib
import binascii


def solve(init_text):
    password = [' '] * 8
    index = 0
    while ' ' in password:
        m = hashlib.md5()
        m.update(binascii.a2b_qp(init_text+str(index)))
        digest = m.hexdigest()
        if digest[0:5] == '00000' and digest[5] in '01234567'and password[int(digest[5])] == ' ':
            password[int(digest[5])] = str(digest[6])
        index +=1
    return "".join(password)


if __name__ == '__main__':
    password = solve('cxdnnyjw')
    print('Secret password is {0}!'.format(password))