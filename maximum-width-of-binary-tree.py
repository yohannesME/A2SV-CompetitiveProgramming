# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def width(self, root, level,tag, output):
        if not root:
            return
        
        output[level].append(tag)

        left = self.width(root.left, level+1, tag*2, output)
        right = self.width(root.right, level+1, tag*2+1, output)

        # if not right and not left:
        #     return [level]
        # elif right and left:
        #     return left + right
        # elif right:
        #     return right
        # else:
        #     return left

        

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        output = defaultdict(list)
        self.width(root, 1,1, output)

        answer = 1
        for value in output.values():
            if len(value) > 1:
                answer = max(answer, value[-1]-value[0]+1 )

        return answer