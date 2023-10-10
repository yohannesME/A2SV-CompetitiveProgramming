# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if root1 and not root2:
            return False
        elif root2 and not root1:
            return False

        dic1 = {}
        dic2 = {}
        
        heap1 = [(root1.val, root1)]
        heap2 = [(root2.val, root2)]

        while heap1 and heap2:
            val1, node1 = heappop(heap1)
            val2, node2 = heappop(heap2)

            if val1 != val2:
                return False
            
            if not node1.right and not node2.right and not node1.left and not node2.right:
                continue
            
            if node1.right:
                heappush(heap1, (node1.right.val, node1.right))
                dic1[node1.right.val] = node1.val
            if node1.left:
                heappush(heap1, (node1.left.val, node1.left))
                dic1[node1.left.val] = node1.val
            if node2.right:
                heappush(heap2, (node2.right.val, node2.right))
                dic2[node2.right.val] = node2.val
            if node2.left:
                heappush(heap2, (node2.left.val, node2.left))
                dic2[node2.left.val] = node2.val

        return dic2 == dic1