# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        visited = set()
        answered = set()

        def dfs(node):
            if not node:
                return ''
            
            left = dfs(node.left)
            right = dfs(node.right)

            i = len(left)
            hash_ = left + 'L'+ str(node.val) +"R" +right + str(i+1)

            if hash_ in visited:
                if hash_ not in answered:
                    answered.add(hash_)
                    ans.append(node)

            visited.add(hash_)
            return hash_

        dfs(root)
        return ans