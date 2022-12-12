class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # went down wrong path if sum > target
        # solution is sum == target
        solutions = []

        def backtracking(target: int, combo: List[int], start: int):
            # A solution, add to answer and stop exploring this path
            print(combo)
            if target == 0: 
                solutions.append(list(combo))
                return
           
            # Not a solution, stop exploring this path
            if target < 0:
                return

            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtracking(target - candidates[i], combo, i)
                combo.pop()

        backtracking(target, [], 0)
        return solutions