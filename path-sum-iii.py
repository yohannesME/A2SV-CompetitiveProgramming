# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        targetSumCount = 0

        def possiblePath(root):
            nonlocal targetSumCount

            if not root:
                return []
            
            left = possiblePath(root.left)
            right = possiblePath(root.right)

            if not left and not right:
                #if the leaf node is the sum then increment our count
                if root.val == targetSum:
                    targetSumCount += 1
                return [root.val]
            
            else:
                #add current value to the coming prefix and see if it equals the target
                newPath = []
                for path in left:
                    newPath.append(path+root.val)
                    if newPath[-1] == targetSum:
                        targetSumCount += 1
                
                for path in right:
                    newPath.append(path+root.val)
                    if newPath[-1] == targetSum:
                        targetSumCount += 1

            #check if current value if equal to target and add it to and return
            if root.val == targetSum:
                targetSumCount += 1
            newPath.append(root.val)

            return newPath
        
        possiblePath(root)

        return targetSumCount