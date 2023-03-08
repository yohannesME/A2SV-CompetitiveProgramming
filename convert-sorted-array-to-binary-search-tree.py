# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self,nums, left, right):
        if right-left == 1:
            return TreeNode(nums[left], None, TreeNode(nums[right]))
        elif right == left:
            return TreeNode(nums[left])

        mid = (right+left)//2
        return TreeNode(nums[mid], self.insert(nums,left, mid-1), self.insert(nums, mid+1, right))
            

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.insert(nums, 0, len(nums)-1)