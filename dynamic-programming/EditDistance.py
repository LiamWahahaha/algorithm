MATCH  = 0
INSERT = 1
DELETE = 2

class Cell:
    def __init__(self):
        self.parent = None
        self.cost = None

class Solution:
    def __init__(self):
        self.path = []
        self.sol = None

    def initialize_table(self, p, t):
        lookup = [[Cell() for _ in range(len(p) + 1)] for _ in range(len(t) + 1)]

        for idx in range(len(p) + 1):
            lookup[0][idx].cost = idx
            lookup[0][idx].parent = INSERT

        for idx in range(len(t) + 1):
            lookup[idx][0].cost = idx
            lookup[idx][0].parent = DELETE

        lookup[0][0].parent = -1

        return lookup

    def print_table(self, lookup, p, t):
        p = ' ' + p
        t = ' ' + t
        print('    ', end = ' ')
        [print('{0:4s}'.format(val), end=' ') for val in p]
        print()

        for idx, row in enumerate(lookup):
            print(t[idx], end=' ')
            [print('{0:4d}'.format(cell.cost), end=' ') for cell in row]
            print()

        print()

    def reconstruct_path(self, lookup, i, j):
        if lookup[i][j].parent == -1:
            return

        if lookup[i][j].parent == MATCH:
            if lookup[i][j].cost == lookup[i-1][j-1].cost:
                self.path.append('M')
            else:
                self.path.append('S')

            self.reconstruct_path(lookup, i-1, j-1)
            return

        if lookup[i][j].parent == INSERT:
            self.path.append('I')
            self.reconstruct_path(lookup, i, j-1)
            return

        if lookup[i][j].parent == DELETE:
            self.path.append('D')
            self.reconstruct_path(lookup, i-1, j)
            return

    def match(self, c1, c2):
        return 0 if c1 == c2 else 1

    def edit_distance(self, p, t):
        lookup = self.initialize_table(p, t)
        opt = [MATCH, INSERT, DELETE] # 0: match, 1: insert, 2: delete

        for idx_i in range(1, len(t) + 1):
            for idx_j in range(1, len(p) + 1):
                opt[MATCH] = lookup[idx_i - 1][idx_j - 1].cost + self.match(t[idx_i - 1], p[idx_j - 1])
                opt[INSERT] = lookup[idx_i][idx_j - 1].cost + 1
                opt[DELETE] = lookup[idx_i - 1][idx_j].cost + 1

                lookup[idx_i][idx_j].cost = opt[MATCH]
                lookup[idx_i][idx_j].parent = MATCH

                for k in range(1, 3):
                    if opt[k] < lookup[idx_i][idx_j].cost:
                        lookup[idx_i][idx_j].cost = opt[k]
                        lookup[idx_i][idx_j].parent = k

        self.sol = lookup[-1][-1].cost
        self.print_table(lookup, p, t)
        self.reconstruct_path(lookup, len(t), len(p))

        return lookup


def testcase():
    t = 'thou-shalt-not'
    p = 'you-should-not'

    sol = Solution()
    lookup = sol.edit_distance(p, t)
    print('the edit distance of', p, 'and', t, 'is:', sol.sol)

    print('the edit sequence from', p, 'to', t, 'is:', end= ' ')
    while sol.path:
        opt = sol.path.pop()
        print(opt, end='')

    print()

if __name__ == '__main__':
    testcase()
