# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        #check both side the tree
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)

        if not right and not left:
            return [root.val]
        elif right and left:
            newList = [root.val]
            if len(right) < len(left):
                newList += right + left[len(right):]
            else:
                newList += right
            return newList
        elif right:
            return [root.val] + right
        else:
            return [root.val] + left