class NQueens:
    def __init__(self):
        self.counter = 0
        self.sol = []

    def is_a_solution(self, arrangement, kth, info):
        return kth == info

    def process_solution(self, arrangement, kth, info):
        ret = []

        for val in arrangement:
            tmp = ['.'] * info
            tmp[val] = 'Q'
            ret.append(tmp)

        self.sol.append(ret)
        self.counter += 1

    def construct_candidates(self, arrangement, kth, info):
        candidates = []

        for col in range(info):
            legal_move = True
            for row in range(kth - 1):
                if arrangement[row] == col:
                    legal_move = False
                if abs(kth - 1 - row) == abs(col - arrangement[row]):
                    legal_move = False

            if legal_move == True:
                candidates.append(col)

        return candidates

    def backtrack(self, arrangement, kth, info):
        if self.is_a_solution(arrangement, kth, info):
            self.process_solution(arrangement, kth, info)
        else:
            kth = kth + 1
            candidates = self.construct_candidates(arrangement, kth, info)
            for candidate in candidates:
                arrangement.append(candidate)
                self.backtrack(arrangement, kth, info)
                arrangement.pop()

    def printSol(self):
        for sol in self.sol:
            for idx_x in range(len(sol)):
                print(sol[idx_x])
            print()

    def solver(self, n):
        if n < 2:
            return 'No solution'

        self.backtrack([], 0, n)
        print(self.counter)
        self.printSol()

def main():
    # case 1:
    NQueens().solver(4)

if __name__ == '__main__':
    main()
