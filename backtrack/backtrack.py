class Combinatorial_Search:
    def __init__(self):
        self.finished = False

    def is_a_solution(self, current_answer, kth, info):
        pass

    def generate_candidates(self, current_answer, kth, info):
        pass

    def process_solution(self, current_answer, kth, info):
        pass

    def backtrack(self, current_answer, kth, info):
        if self.is_a_solution(current_answer, kth, info):
            self.process_solution(current_answer, kth, info)
        else:
            kth += 1
            candidates = self.generate_candidates(current_answer, kth, info)

            for candidate in candidates:
                current_answer.append(candidate)
                self.backtrack(current_answer, kth, info)
                current_answer.pop()
                if self.finished:
                    return
