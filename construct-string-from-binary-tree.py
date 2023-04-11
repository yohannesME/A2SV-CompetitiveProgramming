# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # if not root:
        #     return ''
        # return f'{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})'.replace('()()', '').replace(')()', ')')
        
        #create a list of all values in the string
        ans = [str(root.val)]
        #if we have left we recursively try left
        if root.left:
            ans.append('(' + self.tree2str(root.left) + ')')

        #if we have right we recursively try right
        if root.right:
            #but it was not root left when we encounter right we add empty brace () and continue normally
            if not root.left:
                ans.append('()')
            ans.append('(' + self.tree2str(root.right) + ")")
        
        #finally create the string from the list
        return ''.join(ans)