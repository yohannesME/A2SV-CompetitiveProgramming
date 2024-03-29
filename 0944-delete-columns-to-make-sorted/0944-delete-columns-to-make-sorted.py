class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        output = 0
        
        for column in zip(*strs):

            if ''.join(sorted(column)) != ''.join(column):
                output += 1
        
        return output