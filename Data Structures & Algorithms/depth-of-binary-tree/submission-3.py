# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_d = 0

        def dfs(node):
            nonlocal max_d

            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            cur_max = max(left,right) + 1
            max_d = max(max_d, cur_max)

            return cur_max

        dfs(root)
        return max_d