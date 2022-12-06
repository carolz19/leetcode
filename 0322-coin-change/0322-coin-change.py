from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Find the most optimal solution with backtracking
        @lru_cache(None)
        def backtracking(amount):
            if amount == 0: return 0 # a solution
            if amount < 0: return -1 # went t0o far, not a solution

            count = float('inf') # coins needed
            for coin in coins:
                result = backtracking(amount - coin)
                
                # if result is less than 0, then we must have
                # gone down the wrong path, so we try a different
                # coin
                if result < 0:
                    continue

                # only update count the current path
                # uses less coins that the lowest path seen
                # so far
                count = min(result + 1, count)

            # if count == inf then we didn't get any possible
            # solutions so return -1
            return count if count != float('inf') else -1

        return backtracking(amount)
