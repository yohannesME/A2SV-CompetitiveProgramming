class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinations = []
        def backtrack(index ,currentCombine):
            if len(currentCombine) == k:
                combinations.append(currentCombine[:])
                return
                   

            for i in range(index+1,n+1):
                currentCombine.append(i)
                backtrack(i, currentCombine)
                currentCombine.pop()
        
        for i in range(1, n+1):
            backtrack(i, [i])
        return combinations