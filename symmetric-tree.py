# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #check if 
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val == q.val:
            return True and self.isSameTree(p.right, q.left) and self.isSameTree(p.left, q.right)
        else:
            return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left, root.right)