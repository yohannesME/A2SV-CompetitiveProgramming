# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestPath(self,root):
        if not root:
            #[current value, current count ,maximum count]
            return [1001, 0, 1]
        
        left = self.longestPath(root.left)
        right = self.longestPath(root.right)

        if left[0] == root.val == right[0]:
            #merge
            return [root.val, max(left[1],right[1])+1, max(left[2], right[2], left[1]+right[1]+1) ]
        elif left[0] == root.val:
            #only from the left
            return [root.val, left[1]+1, max(left[2], right[2], left[1]+1) ]

        elif right[0] == root.val:
            #only from the right
            return [root.val, right[1]+1, max(left[2], right[2], right[1]+1) ]
        else:
            return [root.val, 1, max(left[2], right[2])]

        
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        return self.longestPath(root)[2]-1