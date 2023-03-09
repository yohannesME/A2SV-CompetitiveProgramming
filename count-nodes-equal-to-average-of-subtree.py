# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def accumulateAverage(self, root):
        if not root:
            return [0,0,0]
        
        left = self.accumulateAverage(root.left)
        right = self.accumulateAverage(root.right)

        sumOfVal = left[0] + right[0] + root.val
        quantity = left[1] + right[1] + 1

        if root.val == sumOfVal//quantity:
            return [sumOfVal, quantity, left[2]+right[2]+1]

        return [sumOfVal, quantity, left[2]+right[2]]
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.accumulateAverage(root)[2]