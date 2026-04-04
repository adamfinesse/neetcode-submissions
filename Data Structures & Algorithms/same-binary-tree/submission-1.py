# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(n1,n2,sameTree):
            if (not n1 and not n2):
                return [None,None,True]
            if not sameTree or (not n1 and n2) or (n1 and not n2) or (n1.val != n2.val):
                return [None,None, False]
            
            left = same(n1.left,n2.left,True)
            right = same(n1.right,n2.right,True)
            return [None,None, left[2] and right[2]]

        return same(p,q,True)[2]