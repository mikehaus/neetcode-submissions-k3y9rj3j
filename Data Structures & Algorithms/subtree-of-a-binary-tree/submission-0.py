# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # search to find any matching roots
        # if there is a root that starts with the same root, we search that root to see if identical
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
            else:
                return False

        roots = []

        def findStarts(root):
            nonlocal subRoot
            if not root:
                return
            if root and root.val == subRoot.val:
                roots.append(root)
            findStarts(root.left)
            findStarts(root.right)
        
        findStarts(root)
        
        for r in roots:
            if dfs(r, subRoot):
                return True
        return False