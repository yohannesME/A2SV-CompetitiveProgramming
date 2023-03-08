# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def grandSum(self,node, parent=None, grandparent=None):
        if not node:
            return 0

        if grandparent:
            if grandparent.val%2 == 0:
                return node.val + self.grandSum(node.left, node, parent) + self.grandSum(node.right, node, parent) 
        return  self.grandSum(node.left, node, parent) + self.grandSum(node.right, node, parent) 
            
        # if not root:
        #     #[grandchid, child, sum]
        
        #     return [0,0,0]
        
        # left = self.grandSum(root.left)
        # right = self.grandSum(root.right)


        # #add the child
        # if left[1] == 0 and right[1] == 0:
        #     return [0,root.val,0]

        # if root.val % 2 == 0:
        #     return [left[1] + right[1], root.val, left[2]+right[2]+left[0]+right[0]]
        # else:
        #     return [left[1] + right[1], root.val, left[2]+right[2]]



    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.grandSum(root)