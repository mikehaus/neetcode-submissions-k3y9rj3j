class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, path):
            if cur == target:
                res.append(path.copy())
                return
            
            if cur > target or i >= len(nums):
                return
            
            path.append(nums[i])
            dfs(i, cur + nums[i], path)
            path.pop()
            dfs(i + 1, cur, path)

        dfs(0, 0, [])
        return res