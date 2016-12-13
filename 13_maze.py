import heapq


class MazeState(object):
    GOAL = None
    NUM = None
    MAX_STEPS = None

    def __init__(self, x, y, parents=None):
        self.x = x
        self.y = y
        if parents is None:
            self.parents = []
        else:
            self.parents = parents
        self.score = score(x, y, self.GOAL)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return self.score <= other.score

    def __hash__(self):
        return hash((self.x, self.y))

    def next_steps(self):
        """ Make next steps (generator)"""
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            x = self.x + move[0]
            y = self.y + move[1]
            if x < 0 or y < 0:
                continue
            if is_open(x, y, self.NUM):
                if self.MAX_STEPS is None or len(self.parents) < self.MAX_STEPS:
                    yield MazeState(x, y, parents=self.parents + [self])


def score(x, y, goal):
    """ Calculate score based on distance to goal """
    return abs(goal[0] - x) + abs(goal[1] - y)


def is_open(x, y, fav_num):
    """ Check if position is open space """
    number = x * x + 3 * x + 2 * x * y + y + y * y + fav_num
    return bin(number).count('1') % 2 == 0


def solve(num, goal, max_steps=None):
    # Set attributes which are same for all states
    MazeState.GOAL = goal
    MazeState.NUM = num
    MazeState.MAX_STEPS = max_steps

    # Guided search with state scores
    queue = []
    starting_state = MazeState(1, 1)
    heapq.heappush(queue, (starting_state.score, starting_state))
    seen = set()
    seen.add(starting_state)
    steps = 0
    while queue:
        _, item = heapq.heappop(queue)
        seen.add(item)
        if (item.x, item.y) == goal:
            print('The number of steps to {0} is {1}.'.format(goal,len(item.parents)))
            return None
        for new_item in item.next_steps():
            if new_item not in seen:
                heapq.heappush(queue, (new_item.score, new_item))
        steps += 1

    print('The number of states we can reach in {0} steps is {1}'.format(max_steps,len(seen)))
    return None


if __name__ == '__main__':
    solve(1362, (31, 39))
    solve(1362, (1000, 1000), max_steps=50)