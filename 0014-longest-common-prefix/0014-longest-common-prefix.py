class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for i in range(1,len(strs)):
            for j in range(len(common)):
                if j >= len(strs[i]):
                    common = common[:j]
                    break
                if common[j] != strs[i][j]:
                    common = common[:j]
                    break
        return common
            
        