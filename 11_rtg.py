from collections import defaultdict
from itertools import combinations, permutations
from copy import deepcopy
import os
from pymongo import MongoClient

clear = lambda: os.system('cls')


class Factory:
    sol_depth = 0
    elevator = 0
    top_f = 3
    grd_f = 0
    state = []

    def __init__(self, s_dep, ele, state):
        self.sol_depth = s_dep
        self.elevator = ele
        self.state = state

    def check_final(self):
        if sum(self.state[self.top_f]) == len(self.state[self.top_f]):
            print('Solution found at depth {0}.'.format(self.sol_depth))
            return True
        return False

    def state_to_string(self):
        return "".join([str(x) for flr in self.state for x in flr])+str(self.elevator)


def check_fried(state):
    for flr in state:
        tmp = [flr[x]*2 + flr[x+1] for x in range(0,len(flr)-1,2)]
        if 3 in tmp and 1 in tmp: return True
    return False


def generate_combinations(flr, n):
    idxs = [x for x,i in enumerate(flr) if i == 1]
    return combinations(idxs, n)


def are_empty_below(state, flr_num):
    return all([sum(state[x]) == 0 for x in range(0, flr_num)])


def check_visited(collection, state):
    ele = state[-1]
    flrs = state[:-1]
    splits = [flrs[x:x+int(len(flrs)/4)] for x in range(0,len(flrs),int(len(flrs)/4))]
    perms = list(permutations(splits[:-1]))
    for x in perms:
        tmp = "".join(x)+splits[-1]+ele
        if collection.find({'key': tmp}).limit(1).count() > 0:
            return True
    return False


def generate_successor_factories(fac, collection):
    generated = []

    ele_moves = [x for x in range(-1,2,2) if fac.grd_f <= fac.elevator + x <= fac.top_f]
    itm_moves = [x for x in range(1,min(2,sum(fac.state[fac.elevator]))+1)]

    crr_flr = deepcopy(fac.state[fac.elevator])

    for i_m in itm_moves:
        idxs = list(generate_combinations(crr_flr, i_m))
        for idx in idxs:
            itms = [x for x in idx]
            for e_m in ele_moves:
                crr_state = deepcopy(fac.state)

                if e_m == -1 and any([len(x) == 1 for x in idxs]) and len(idx) == 2: continue
                if e_m == 1 and any([len(x) == 2 for x in idxs]) and len(idx) == 1: continue
                if e_m == -1 and are_empty_below(crr_state, fac.elevator): continue

                for itm in itms:
                    crr_state[fac.elevator + e_m][itm] = 1
                    crr_state[fac.elevator][itm] = 0
                if not check_fried(crr_state):
                    f = Factory(fac.sol_depth+1,fac.elevator + e_m,crr_state)
                    if not check_visited(collection,f.state_to_string()):
                        collection.insert_one({'key': f.state_to_string()})
                        generated.append(f)

    return generated

if __name__ == '__main__':
    part1_state = [[1,1,1,0,1,0,0,0,0,0],
                   [0,0,0,1,0,1,0,0,0,0],
                   [0,0,0,0,0,0,1,1,1,1],
                   [0,0,0,0,0,0,0,0,0,0]]
    part2_state = [[1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                   [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    dummy_state = [[0,1,0,1],
                   [1,0,0,0],
                   [0,0,1,0],
                   [0,0,0,0]]

    crr = Factory(0,0,part2_state)
    depth = 0
    counter = 0
    to_check = []

    client = MongoClient('localhost', 27017)
    collection = client.advent.eleven

    collection.insert_one({'key': crr.state_to_string()})

    while not crr.check_final():
        counter += 1
        if crr.sol_depth > depth:
            depth = crr.sol_depth
            print("Exploring solutions on depth {0}, checked {1} states"
                  ", still need to check at least {2} states.".format(depth,counter, len(to_check)))
        to_check += generate_successor_factories(crr, collection)
        crr = to_check.pop(0)