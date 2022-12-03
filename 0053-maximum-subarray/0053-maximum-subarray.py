class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArray = currSubArray = nums[0]
        for num in nums[1:]:
            currSubArray = max(num, currSubArray + num)
            maxSubArray = max(maxSubArray, currSubArray)

        return maxSubArray