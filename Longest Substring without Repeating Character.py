class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strMap = {}
        longest = 0
        start, end = 0, 0
        count = 0
        while end < len(s):
            if s[end] in strMap:
                # longest = max(len(strMap),longest)
                start += 1
                end = start
                strMap = {}
                strMap[s[end]] = True
                
                
            else:
                strMap[s[end]] = True
                longest = max(longest, end-start + 1)
            # print(longest, start, end, (s[end] in strMap), strMap)
            end += 1
        return longest

        
