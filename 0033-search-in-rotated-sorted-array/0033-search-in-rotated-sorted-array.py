class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        # Perform binary search
        while l <= r:
            m = (r - l) // 2 + l

            if nums[m] == target:
                return m

            # if value at l less than m, we know left side is sorted
            # else some numbers on left are bigger, but we know right side is sorted
            if nums[l] <= nums[m]:
                # Check if target in left side
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # Check if target in right side
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1