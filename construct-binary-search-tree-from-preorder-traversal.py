# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def createTree(root, num):
            if root.val > num:
                if root.left:
                    createTree(root.left, num)
                else:
                    root.left = TreeNode(num)
            else:
                if root.right:
                    createTree(root.right, num)
                else:
                    root.right = TreeNode(num)
                    
        root = TreeNode(val=preorder[0])
        for i in range(1, len(preorder)):
            createTree(root, preorder[i])

        
        return root