class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(start):
            if start >= len(nums):
                res.append(path.copy())
                return

            path.append(nums[start])
            dfs(start + 1)
            path.pop()
            dfs(start + 1)
        
        dfs(0)
        return res