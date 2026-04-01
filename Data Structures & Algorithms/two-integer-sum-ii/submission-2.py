class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        l, r = 0, len(nums) - 1

        while l < r:
            sum = nums[l] + nums[r]
            if sum == target and l != r:
                return [l + 1, r + 1]
            elif sum > target:
                r -= 1
            else:
                l += 1

        return res
