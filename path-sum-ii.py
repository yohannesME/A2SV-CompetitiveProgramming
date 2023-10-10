# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        if not root.left and not root.right:
            return [[root.val]] if root.val == targetSum else []
        
        path = {}
        ans = []

        i = 0
        heap = [(root.val, i , root)]

        while heap:
            val, j , node = heappop(heap)

            if not node.left and not node.right:
                if val == targetSum:
                    targetpath = [node.val]
                    t = path[node]
                    while t != root :
                        targetpath.append(t.val)
                        t = path[t]
                    targetpath.append(root.val)
                    targetpath.reverse()
                    ans.append(targetpath)
            
            if node.right:
                i += 1
                heappush(heap, (node.right.val + val, i, node.right))
                path[node.right] = node
            
            if node.left:
                i += 1
                heappush(heap, (node.left.val + val, i, node.left))
                path[node.left] = node
        
        return ans