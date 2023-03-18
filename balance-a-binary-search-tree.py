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
           


    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def traverse(root):
            if not root:
                 return

            traverse(root.left)
            nums.append(root.val)
            traverse(root.right)
        
        traverse(root)

        return self.insert(nums, 0, len(nums)-1)