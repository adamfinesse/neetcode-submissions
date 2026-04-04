# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(n1,n2):
            if not n1 and not n2:
                return True
            if not n1 and n2 or n1 and not n2 or n1.val != n2.val:
                return False
            left = sameTree(n1.left,n2.left)
            right = sameTree(n1.right,n2.right)

            return left and right

        def dfs(node):
            if not node:
                return False
            if node.val == subRoot.val and sameTree(node,subRoot):
                return True
        
            return dfs(node.left) or dfs(node.right)
            
        return dfs(root)