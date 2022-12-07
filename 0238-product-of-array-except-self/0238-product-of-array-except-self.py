class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1] # products of numbers to the left of i in nums
        R = [1] # # products of numbers to the right of i in nums
        answers = []

        prod = 1
        for num in nums[:len(nums)]:
            prod *= num
            L.append(prod)

        prod = 1
        for num in reversed(nums[1:]):
            prod *= num
            R.append(prod)

        # combine L and R to get product of array except self
        for l, r in zip(L, reversed(R)):
            answers.append(l*r)

        return answers