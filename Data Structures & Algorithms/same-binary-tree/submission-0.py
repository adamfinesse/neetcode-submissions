# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        sameTree = True
        def same(n1,n2):
            nonlocal sameTree

            if (not n1 and not n2) or not sameTree:
                return
            #print(n1,n2)
            if (not n1 and n2) or (n1 and not n2) or (n1.val != n2.val):
                sameTree = False
                return
            
            same(n1.left,n2.left)
            same(n1.right,n2.right)
        same(p,q)
        return sameTree