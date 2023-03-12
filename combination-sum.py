class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(index=0,currentSumList=[]):

            if index >= len(candidates):
                return 

            currentSum = sum(currentSumList)
            
            if currentSum == target:
                output.append(currentSumList)
                return
            elif currentSum > target:
                return
            

            for i in range(index, len(candidates)):
                backtrack(i, currentSumList+[candidates[i]])
        
        backtrack()
        return output