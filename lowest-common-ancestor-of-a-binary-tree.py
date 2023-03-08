# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def common(self,root, p, q):
        if not root:
            return [0, None]
        
                
        left = self.common(root.left, q, p)
        right = self.common(root.right, q, p)
       
        if (root == p or root == q):
            if right[0] + left[0] > 0:
                return [2, root]
            else:
                return [1, root]
        else:
            if left[0] == 1 and right[0] == 1:
                return [2,root]
            elif left[0] != 0:
                return left
            elif right[0] != 0:
                return right

            return [0, None]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.common(root, p, q)[1]