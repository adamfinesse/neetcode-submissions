# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s = [root]
        while root.left: 
            s.append(root.left)
            root = root.left

        res = []
        while s:
            node = s.pop()
            
            # if node.left: 
            #     s.append(node.left)

            res.append(node.val)

            if node.right:
                s.append(node.right)
                if node.right.left:
                    s.append(node.right.left)
        return res
            


        