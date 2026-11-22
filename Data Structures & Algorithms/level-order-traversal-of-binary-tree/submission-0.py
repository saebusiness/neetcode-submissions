# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = [[]]
        if not root:
            return []
        stack = deque([root, "#"])

        while stack:
            
            cur = stack.popleft()
            if len(stack) == 0:
                break
            if cur == "#":
                stack.append("#")
                ans.append([])
                continue
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            ans[-1].append(cur.val)

        return ans
            
