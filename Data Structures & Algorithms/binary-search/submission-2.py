class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            mid = nums[m]
            if mid == target:
                return m
            elif mid < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1