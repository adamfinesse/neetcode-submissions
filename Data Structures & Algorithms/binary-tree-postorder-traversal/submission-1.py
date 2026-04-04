# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        s = []
        cur = root

        while s or cur:
            while cur:
                s.append((cur,1))
                if cur.right:
                    s.append((cur.right,0))
                cur = cur.left
            node,seen_count = s.pop()
            if seen_count == 1:
                res.append(node.val)
            else:
                cur = node
            
        return res
                
