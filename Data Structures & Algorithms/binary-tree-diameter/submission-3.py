# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0
        if not root:
            return 0

        def diameter(node):
            nonlocal max_d
            if not node:
                return 0
            left = diameter(node.left)
            right = diameter(node.right)
            max_d = max(max_d, left + right)
            return max(left, right) + 1
        
        diameter(root)
        return max_d