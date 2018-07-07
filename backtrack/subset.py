class Subset:
    def __init__(self):
        self.finished = False
        self.result = []

    def is_a_solution(self, a, k, n):
        return k == len(n)

    def construct_candidates(self, a, k, n):
        return [True, False]

    def process_solution(self, a, k, n):
        self.result.append([n[idx] for idx, val in enumerate(a) if val])

    def recursive(self, nums):
        res = [0 for _ in nums]
        self.backtrack(res, 0, nums)
        return self.result

    def backtrack(self, a, k, n):
        if self.is_a_solution(a, k, n):
            return self.process_solution(a, k, n)
        else:
            k = k + 1
            c = self.construct_candidates(a, k, n)
            for val in c:
                a[k-1] = val
                self.backtrack(a, k, n)

print(Subset().recursive([1,2,3]))
