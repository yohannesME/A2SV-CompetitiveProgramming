# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(root, canRob, memo={}):
            if not root:
                return 0
            
            if (root, canRob) in memo:
                return memo[(root, canRob)]
            
            if canRob:
                memo[(root,canRob)] = max(root.val + dp(root.left, False) + dp(root.right, False), dp(root.left , True) + dp(root.right, True))
            else:
                memo[(root, canRob)] =  dp(root.left , True) + dp(root.right, True)
            
            return memo[(root, canRob)]

        return max(dp(root,True), dp(root,False))