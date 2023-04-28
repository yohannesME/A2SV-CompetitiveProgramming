# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque([root])
        acc = root.val
        
        while queue:
            ans.append(acc/len(queue))
            acc = 0
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    acc += node.left.val
                if node.right:
                    queue.append(node.right)
                    acc += node.right.val

        return ans