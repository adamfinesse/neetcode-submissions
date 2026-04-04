# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qu = [(p,q)]

        while qu:
            for i in range(len(qu)):
                n1,n2 = qu.pop()
                if not n1 and not n2:
                    continue
                if not n1 and n2 or n1 and not n2 or n1.val != n2.val:
                    return False
    
                qu.append((n1.left,n2.left))
                qu.append((n1.right,n2.right))
        return True
