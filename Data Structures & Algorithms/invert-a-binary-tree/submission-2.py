# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = [root]
        while s:
            print(s)
            node = s.pop()
            if not node or not node.left and not node.right:
                continue
            node.left,node.right = node.right, node.left
            s.append(node.left)
            s.append(node.right)
        return root