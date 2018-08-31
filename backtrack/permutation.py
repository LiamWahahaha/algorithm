from combinatorial_search import Backtracking

class Permutation(Backtracking):
    def is_a_solution(self, current_answer, kth, info):
        return kth == len(info)

    def generate_candidates(self, current_answer, kth, info):
        return [candidate for candidate in info if candidate not in current_answer]

    def process_solution(self, current_answer, kth, info):
        print(current_answer)

    def permute(self, info):
        self.backtrack([], 0, info)

def main():
    # case 1
    Permutation().permute([1, 2, 3])

if __name__ == '__main__':
    main()
