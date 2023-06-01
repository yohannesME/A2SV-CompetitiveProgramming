class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}
        maximum = 1

        for i in range(len(arr)):
            if arr[i] - difference in memo:
                memo[arr[i]] = 1 + memo[arr[i] - difference]
                maximum = max(maximum, memo[arr[i]])
            else:
                memo[arr[i]] = 1
        
        return maximum