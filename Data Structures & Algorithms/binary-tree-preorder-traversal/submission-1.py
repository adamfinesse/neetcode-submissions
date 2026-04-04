# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = []
        cur = root

        res = []
        while s or cur:
            while cur:
                res.append(cur.val)
                s.append(cur)
                cur = cur.left
            
            node = s.pop()
    
            if node.right:
                cur = node.right

        return res
            
