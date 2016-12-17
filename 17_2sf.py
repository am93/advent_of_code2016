import heapq
import hashlib
import binascii

class MazeState(object):
    GOAL = None
    SALT = None

    def __init__(self, x, y, path=None):
        self.x = x
        self.y = y
        if path is None:
            self.path = []
        else:
            self.path = path

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
       return len(self.path) <= len(other.path)

    def __hash__(self):
        return hash((self.x, self.y))

    def next_steps(self):
        """ Make next steps (generator)"""
        m = hashlib.md5()
        m.update(binascii.a2b_qp(self.SALT+''.join(self.path)))
        digest = m.hexdigest()
        moves = [((0, -1),'U'), ((0, 1),'D'), ((-1, 0),'L'), ((1, 0),'R')]
        for i, move in enumerate(moves):
            x = self.x + move[0][0]
            y = self.y + move[0][1]
            if x < 0 or y < 0 or x > 3 or y > 3 or (self.x == 3 and self.y == 3):
                continue
            if is_open(i, digest):
                yield MazeState(x, y, path=self.path + [move[1]])


def is_open(move_idx, digest):
    """ Check if position is open space """
    if digest[move_idx] in 'bcdef':
        return True
    return False


def solve(salt, goal, longest=False):
    # Set attributes which are same for all states
    MazeState.GOAL = goal
    MazeState.SALT = salt

    # Guided search with state scores
    queue = []
    starting_state = MazeState(0, 0)
    heapq.heappush(queue, (len(starting_state.path), starting_state))
    max_len = -1
    while queue:
        _, item = heapq.heappop(queue)
        if (item.x, item.y) == goal:
            if not longest:
                print('The shortest path to {0} is {1} of length {2}.'.format(goal,"".join(item.path), len(item.path)))
                return None
            else:
                if max_len < len(item.path):
                    max_len = len(item.path)
                    print(max_len)
        for new_item in item.next_steps():
            heapq.heappush(queue, (len(new_item.path), new_item))

    print('The longest path to {0} has length {1}.'.format(goal, max_len))
    return None


if __name__ == '__main__':
    solve('udskfozm',(3,3),longest=True)