# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(rootp, rootq):
            if not rootp and not rootq:
                return True
            if not rootp and rootq:
                return False
            if rootp and not rootq:
                return False
            if not rootp.val == rootq.val:
                return False
            return dfs(rootp.left, rootq.left) and dfs(rootp.right, rootq.right)

        return dfs(p, q)