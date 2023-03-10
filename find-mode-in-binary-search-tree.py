# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def modeFinding(self, root, output=[[],0]):
    #     #answer consist of [past node value, current count of values of the node, maximum encountered]
    #     if not root:
    #         return
        

    #     left = self.modeFinding(root.left, output)
    #     right = self.modeFinding(root.right, output)


    #     if not left and not right:
    #         return [root.val, 1, 1]

    #     elif left and right:
    #         #check to see which value will continue
    #         #four choices the left, right , root.val
    #             #all 3 are equal
    #             # two of the three are equal - two choices here
    #             # all are different
    #             if left[0] == right[0] == root.val:
    #                 return [root.val, left[1]+right[1]+1, max(left[1]+right[1]+1, left[2], right[2])]
    #             elif left[0] == root.val:
    #                 return [root.val, left[1] + 1, max(left[1]+ 1, left[2], right[2])]
    #             elif right[0] == root.val:
    #                 return [root.val, right[1] + 1, max(right[1]+ 1, left[2], right[2])]
    #             else:
    #                 return [root.val, 1, max(right[2], left[2])]
    #     elif left:
    #         #only from the left
    #         if root.val == left[0]:
    #             left[1] += 1
    #             left[2] = max(left[2], left[1])
    #             return left
    #         else:
    #             return [root.val, 1, left[2]]
    #     else:
    #         #only from the right
    #         if root.val == right[0]:
    #             right[1] += 1
    #             right[2] = max(right[2], right[1])
    #             return right
    #         else:
    #             return [root.val, 1, right[2]]
    def mapImplementation(self, root, output):
        if not root:
            return
        output.append(root.val)
        self.mapImplementation(root.left, output)
        self.mapImplementation(root.right, output)
        


    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        answer = []
        
        self.mapImplementation(root, output)
        count = Counter(output)
        maximum = max(count.values())
        print(count.items())
        for value, count in count.items():
            if maximum == count:
                answer.append(value)
        
        return answer