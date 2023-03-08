# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #if no distance just return the target to be the element
        if k == 0:
            return [target.val]
        
        output = []

        def calcDistance(root, target, k):
            
            nonlocal output
            if not root:
                return []
            
            left = calcDistance(root.left, target,k)
            right = calcDistance(root.right, target,k)
            if not left and not right:
                #update the distance if we find the target to be edge
                if root.val == target:
                    return 1
                return [[root.val]]
            
            #arrays is returned and create a new array with merged and updated values
            if type(left) == type(right):
                newDistance = [[root.val]]
                if len(left) < len(right):
                    for index,val in enumerate(left):
                        right[index] += val
                    newDistance += right
                else:
                    for index,val in enumerate(right):
                        left[index] += val
                    newDistance += left

                #check if target
                if root.val == target:
                    if len(newDistance) > k:
                        output += newDistance[k]
                    return 1
                else:
                    return newDistance
            #if one of the values is the distance then check if k is present by substracting distance
            elif type(left) == type([]):
                newDistance = [[root.val]]+left
                #calculate the distance
                if len(newDistance) > k-right and k >= right:
                    output += newDistance[k-right]
                return right+1

            elif type(right) == type([]):
                newDistance = [[root.val]]+right
                #calculate the distance
                if len(newDistance) > k-left and k >= left:
                    output += newDistance[k-left]
                
                return left + 1
        calcDistance(root, target.val,k)
        return output