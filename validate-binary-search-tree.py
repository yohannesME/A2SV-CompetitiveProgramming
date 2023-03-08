# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkValid(self, root, low=float('-inf'), high=float('inf')):
        if not root:
            return True
        else:
            return (low < root.val < high) and self.checkValid(root.left, low, root.val) and self.checkValid(root.right, root.val , high)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValid(root)