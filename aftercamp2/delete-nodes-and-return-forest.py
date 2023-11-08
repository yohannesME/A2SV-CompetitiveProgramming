# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # edge case no root
        if not root:
            return []

        # first make to_delete a set for O(1) check
        to_delete = set(to_delete)

        #forest array
        forest = []

        def collectForest(node, shouldAdd):
            if not node:
                return
            
            left = False
            right = False

            if node.left and node.left.val in to_delete:
                collectForest(node.left, True) 
                left = True
                node.left = None

            if node.right and node.right.val in to_delete:
                right = True
                collectForest(node.right, True) 
                node.right = None
            
            
            if shouldAdd:
                if not left and node.left:
                    forest.append(node.left)
                    collectForest(node.left, False)
                if not right and node.right:
                    forest.append(node.right)
                    collectForest(node.right, False)            
            else:
                if not left:
                    collectForest(node.left, False)
                if not right:
                    collectForest(node.right, False)

        if root.val not in to_delete:
            forest.append(root)

        collectForest(root, root.val in to_delete)
        return forest 
