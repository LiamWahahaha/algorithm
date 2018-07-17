class Cell:
    def __init__(self):
        self.parent = None
        self.cost = None

class Solution:
    def initialize_table(self, p, t):
        lookup = [[Cell() for _ in range(len(p) + 1)] for _ in range(len(t) + 1)]

        for idx in range(len(p) + 1):
            lookup[0][idx].cost = idx

        for idx in range(len(t) + 1):
            lookup[idx][0].cost = idx

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

    def match(self, c1, c2):
        return 0 if c1 == c2 else 1

    def edit_distance(self, p, t):
        lookup = self.initialize_table(p, t)
        opt = [0, 1, 2] # 0: match, 1: insert, 2: delete

        for idx_i in range(1, len(t) + 1):
            for idx_j in range(1, len(p) + 1):
                opt[0] = lookup[idx_i - 1][idx_j - 1].cost + self.match(t[idx_i - 1], p[idx_j - 1])
                opt[1] = lookup[idx_i][idx_j - 1].cost + 1
                opt[2] = lookup[idx_i - 1][idx_j].cost + 1

                lookup[idx_i][idx_j].cost = opt[0]
                lookup[idx_i][idx_j].parent = 0

                for k in range(1, 3):
                    if opt[k] < lookup[idx_i][idx_j].cost:
                        lookup[idx_i][idx_j].cost = opt[k]
                        lookup[idx_i][idx_j].parent = k

        self.print_table(lookup, p, t)

        return lookup[-1][-1].cost


def testcase():
    p = 'thou-shalt-not'
    t = 'you-should-not-'

    print('the edit distance of', p, 'and', t, 'is:', Solution().edit_distance(p, t))

if __name__ == '__main__':
    testcase()
