# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        potentialMax = -1001
        def traverse(root):
            nonlocal potentialMax
            if not root:
                return 0
            
            left = traverse(root.left)
            right = traverse(root.right)


            val =  max(root.val, root.val+left, root.val+right)
            potentialMax = max(potentialMax, left+right+root.val, val)
            return val
        
        traverse(root)
        return potentialMax