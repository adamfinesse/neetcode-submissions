# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        s = [(root,1)]
        m = 0
        while s:
            node,cnt = s.pop()
            m = max(m,cnt)
            if node and node.left:
                s.append((node.left,cnt+1))
            if node and node.right:
                s.append((node.right,cnt+1))
        return m