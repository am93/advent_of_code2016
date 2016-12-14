import hashlib
import binascii


def has_repeated(hashed, n=3, pattern=None):
    if pattern is None:
        reps = [hashed[x:x+n] for x in range(len(hashed)-(n-1)) if hashed[x]*n == hashed[x:x+n]]
    else:
        reps = [hashed[x:x+n] for x in range(len(hashed)-(n-1)) if pattern == hashed[x:x+n]]
    if len(reps) > 0:
        return reps[0]
    else:
        return None


def update_hash_cache(hashes, key, second=False):
    m = hashlib.md5()
    if key in hashes.keys():
        return hashes[key]
    else:
        if second:
            digest = key
            for _ in range(2017):
                m = hashlib.md5()
                m.update(binascii.a2b_qp(digest))
                digest = m.hexdigest()
            hashes[key] = digest
            return hashes[key]

        else:
            m.update(binascii.a2b_qp(key))
            hashes[key] = m.hexdigest()
            return hashes[key]


def solve(init_text):
    hashes = {}
    keys = []
    candidate = None
    trip = None
    idx_m = 0
    idx_c = 0
    while len(keys) < 64:
        if candidate is None:
            digest = update_hash_cache(hashes, init_text + str(idx_m), True)
            trip = has_repeated(digest)
            if trip is not None:
                candidate = digest
                idx_c = 1
            else:
                idx_m += 1
        else:
            if idx_c > 1000:
                candidate = None
                idx_m += 1
                continue
            digest = update_hash_cache(hashes, init_text + str(idx_m+idx_c), True)
            reps = has_repeated(digest, 5, trip[0]*5)
            if reps is not None:
                keys.append(candidate)
                idx_c = 1001
                print('Current idx {0}, current number of keys {1}'.format(idx_m,len(keys)))
            else:
                idx_c += 1
    return idx_m

if __name__ == '__main__':
    solution = solve('ahsbgdzn')
    print('Secret password is {0}!'.format(solution))