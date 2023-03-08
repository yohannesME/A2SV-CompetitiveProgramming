# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeGreater(self,root,add=0):
        if not root:
            return add

        right = self.makeGreater(root.right, add)

        root.val += right

        left = self.makeGreater(root.left, root.val)

        return left     

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.makeGreater(root)
        return root