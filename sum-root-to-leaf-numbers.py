# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0

        #each time accumulate the value and when we return release them
        def dfs(acc, root):
            nonlocal answer
            if not root:
                return
            
            acc = acc*10+root.val

            if not root.left and not root.right:
                answer += acc
                acc //= 10
                return

            dfs(acc, root.left)
            dfs(acc, root.right)
    
        dfs(0,root)
        return answer