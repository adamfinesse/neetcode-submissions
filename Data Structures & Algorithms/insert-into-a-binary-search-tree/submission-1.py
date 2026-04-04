# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        if not root:
            return TreeNode(val)
        while True:
            if cur and cur.val > val and cur.left:
                cur = cur.left
            elif cur and cur.val > val and not cur.left:
                cur.left = TreeNode(val,None,None)
                return root
            
            if cur and cur.val < val and cur.right:
                cur = cur.right
            elif cur and cur.val < val and not cur.right:
                cur.right = TreeNode(val,None,None)
                return root
        return root