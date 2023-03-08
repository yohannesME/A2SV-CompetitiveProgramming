# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return [[str(root.val)]]
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        newPath = []

        if left and right:
            newPath = left + right
        elif left:
            newPath = left
        elif right:
            newPath = right

        for path in newPath:
            path.append(str(root.val))
        return newPath

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        possiblePath = self.traverse(root)
        output = []
        for path in possiblePath:
            output.append('->'.join(path[::-1]))
        return output