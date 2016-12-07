def check_palindrome(sample):
    return sample == sample[::-1] and sample[0] != sample[1] and '[' not in sample and ']' not in sample


def update_aba(sample, ob_count, cb_count, palindromes):
    if check_palindrome(sample) and ob_count == cb_count:
        if sample in palindromes.keys(): palindromes[sample][0] += 1
        else: palindromes[sample] = [1,0]
    return palindromes


def update_bab(sample, ob_count, cb_count, palindromes):
    sample_aba = sample[1] + sample[0] + sample[1]
    if check_palindrome(sample) and ob_count > cb_count:
        if sample_aba in palindromes.keys(): palindromes[sample_aba][1] += 1
        else: palindromes[sample_aba] = [0,1]
    return palindromes


def check_valid_tls(palindromes, brackets):
    return len(palindromes) and not any([b[0] < p < b[1] for p in palindromes for b in brackets])


def check_valid_ssl(palindromes):
    return any([p[0] > 0 and p[1] > 0 for _,p in palindromes.items()])


def solve_tls(filename):
    f = open(filename)
    count = 0
    for line in f:
        brackets = []
        palindromes = []
        cb_count = 0
        stripped = line.strip()
        for x in range(len(stripped)-3):
            if stripped[x] == '[' :
                brackets.append([x,-1])
                continue
            if stripped[x] == ']' :
                brackets[cb_count][1] = x
                cb_count += 1
                continue
            if check_palindrome(stripped[x:x+4]): palindromes.append(x)
        count += int(check_valid_tls(palindromes, brackets))

    f.close()
    return count


def solve_ssl(filename):
    f = open(filename)
    count = 0
    for line in f:
        palindromes = {}
        ob_count = 0
        cb_count = 0
        stripped = line.strip()
        for x in range(len(stripped)-2):
            if stripped[x] == '[' :
                ob_count += 1
                continue
            if stripped[x] == ']' :
                cb_count += 1
                continue
            update_aba(stripped[x:x+3],ob_count,cb_count,palindromes)
            update_bab(stripped[x:x+3],ob_count,cb_count,palindromes)
        count += int(check_valid_ssl(palindromes))

    f.close()
    return count

if __name__ == '__main__':
    result_tls = solve_tls('data/07_tls.data')
    result_ssl = solve_ssl('data/07_tls.data')
    print("TLS: {0}, SSL: {1}".format(result_tls, result_ssl))