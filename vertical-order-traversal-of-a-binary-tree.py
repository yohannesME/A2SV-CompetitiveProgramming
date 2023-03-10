# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        outputs = defaultdict(list)

        def traverse(root, row, col, outputs):
            if not root:
                return 

            outputs[col].append([row,root.val])
            traverse(root.right, row+1, col-1, outputs)
            traverse(root.left, row+1, col+1, outputs)
        
        traverse(root, 0,0,outputs)
        answer = []

        for key, nums in sorted(outputs.items(), reverse=True):
            nums.sort()
            num = []
            for row, value in nums:
                num.append(value)
            answer.append(num)
        return answer