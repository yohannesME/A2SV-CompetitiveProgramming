# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, output, height ):
        if not root:
            return

        if len(output) >= height:
            #as zero indexed
            output[height - 1].append(root.val)
        else:
            output.append([root.val])

        self.traverse(root.left, output, height + 1)
        self.traverse(root.right, output, height + 1)
        
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        
        self.traverse(root, output, 1)
        return output