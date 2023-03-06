# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        def traverse(root):
            if root:
                inorder.append(root.val)
                if root.left:
                    traverse(root.left)
                if root.right:
                    traverse(root.right)
        traverse(root)
        return inorder