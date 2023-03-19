# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        #get the maximum values index from a given array.
        maxIndex = max(range(len(nums)), key=nums.__getitem__)
        #inputs that value and recursively call it one the left and right side of tree
        return TreeNode(nums[maxIndex],self.constructMaximumBinaryTree(nums[:maxIndex]), self.constructMaximumBinaryTree(nums[maxIndex+1:]))