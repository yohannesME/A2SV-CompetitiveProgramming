# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = 0
        answer = -1
        def find(root,k):
            nonlocal current
            nonlocal answer

            if not root or answer != -1:
                return
            
            find(root.left,k)

            current += 1
            if current == k:
                answer = root.val

            find(root.right,k) 
        
        find(root,k )
        return answer