# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True
        def dfs(node,min_val,max_val):
            nonlocal isValid
            if not node or not isValid:
                return
            if node.val <= min_val or node.val >= max_val:
                isValid = False
                return
            dfs(node.left, min_val,node.val)
            dfs(node.right,node.val,max_val)

        dfs(root,float('-inf'),float("inf"))
        return isValid

