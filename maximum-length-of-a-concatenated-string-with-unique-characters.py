class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniqueMaxLen = 0
        N = len(arr)

        def backtrack(index, uniqueSet=set()):
            nonlocal uniqueMaxLen, N
            
            currSize = len(uniqueSet)
            uniqueMaxLen = max(uniqueMaxLen, currSize)


            for i in range(index, N):
                merged = uniqueSet.union(set(arr[i]))
                if len(merged) == len(arr[i]) + currSize:
                    backtrack(i+1, merged)
        
        backtrack(0)
        return uniqueMaxLen