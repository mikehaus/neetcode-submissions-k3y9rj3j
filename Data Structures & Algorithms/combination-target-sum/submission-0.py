class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(0, nums, target, res, 0, [])
        return res

    def dfs(self, i, nums, target, res, cur_sum, path):
        if cur_sum == target:
            res.append(path.copy())
            return

        if cur_sum > target or i >= len(nums):
            return 

        path.append(nums[i])
        self.dfs(i, nums, target, res, cur_sum + nums[i], path)
        path.pop()

        self.dfs(i + 1, nums, target, res, cur_sum, path)