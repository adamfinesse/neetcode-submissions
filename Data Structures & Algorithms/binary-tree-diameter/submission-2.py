# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d=0
        def diameter(node):
            nonlocal d
            if not node:
                return 0
            
            left_depth = diameter(node.left)
            right_depth = diameter(node.right)
            d = max(left_depth+right_depth,d)
            return 1 + max(left_depth,right_depth)
           
        diameter(root)
        return d