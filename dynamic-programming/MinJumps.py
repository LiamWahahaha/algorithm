class MinJumps:
    def __init__(self, elems):
        self.sol = None
        self.elems = elems
        self.elem_len = len(elems)

    def input_checking(self):
        return (self.elem_len == 0 or self.elems[0] == 0)

    def min_jumps(self):
        if self.input_checking():
            return float('inf')

        lookup_table = [[False, None] for _ in self.elems]
        lookup_table[0] = [True, None]
        goal = self.elem_len - 1
        idx = 0

        while idx <=  goal:
            if not lookup_table[idx][0]:
                return -1

            movement = self.elems[idx]

            if idx + movement >= goal:
                lookup_table[-1] = [True, idx]
                break
            else:
                for pos in range(idx + 1, idx+ movement + 1):
                    if not lookup_table[pos][0]:
                        lookup_table[pos] = [True, idx]
            idx += 1

        count = 1
        parent = lookup_table[-1]
        path = [self.elems[-1]]

        while parent[1]:
            path.append(self.elems[parent[1]])
            parent = lookup_table[parent[1]]
            count += 1

        path.append(self.elems[0])
        print(path[::-1])

        return count

    def left_right(self):
        if self.input_checking():
            return float('inf')

        jumps = [0 for _ in range(self.elem_len)]

        for idx_i in range(1, self.elem_len):
            jumps[idx_i] = float('inf')

            for idx_j in range(idx_i):
                if idx_i <= idx_j + self.elems[idx_j] and jumps[idx_j] != float('inf'):
                    jumps[idx_i] = min(jumps[idx_i], jumps[idx_j] + 1)
                    break

        return jumps[self.elem_len - 1]

    def right_left(self):
        if self.input_checking():
            return float('inf')

        jumps = [0 for _ in range(self.elem_len)]

        for idx_i in range(self.elem_len - 2, -1, -1):
            if self.elems[idx_i] == 0:
                jumps[idx_i] = float('inf')
            elif idx_i + self.elems[idx_i] >= self.elem_len - 1:
                jumps[idx_i] = 1
            else:
                min = float('inf')

                for idx_j in range(idx_i + 1, self.elem_len):
                    if (idx_j <= self.elems[idx_i] + idx_i):
                        if (min > jumps[idx_j]):
                            min = jumps[idx_j]

                if (min != float('inf')):
                    jumps[idx_i] = min + 1
                else:
                    jumps[idx_i] = min

        return jumps[0]

def testcase():
    test1 = MinJumps([1,3,5,8,9,2,6,7,6,8,9])
    test2 = MinJumps([1,3,6,1,0,9])
    test3 = MinJumps([])
    print('mine:', test1.min_jumps())
    print('left right:', test1.left_right())
    print('right left:', test1.right_left())

    print('mine:', test2.min_jumps())
    print('left right:', test2.min_jumps())
    print('mine:', test3.min_jumps())
    print('left right:', test3.min_jumps())

def main():
    testcase()

if __name__ == '__main__':
    main()
