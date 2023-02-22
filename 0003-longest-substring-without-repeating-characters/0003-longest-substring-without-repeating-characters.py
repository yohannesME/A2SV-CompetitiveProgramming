class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #intialize
        strMap = {}
        longest = 0
        start = 0
        end = 0
        count = 0
        
        #while not in the end
        while end < len(s):
            #reset if encountered again
            if s[end] in strMap:
                start += 1
                end = start
                strMap = {}
                strMap[s[end]] = True
            #if not just continue and add the window size  
            else:
                strMap[s[end]] = True
                longest = max(longest, end-start + 1)
                
            end += 1
        return longest

        