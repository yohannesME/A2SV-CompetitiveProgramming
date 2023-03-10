class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(index, current):
            output.append(current[:])

            for i in range(index, len(nums)):
                backtrack(i+1, current + [nums[i]])
        
        backtrack(0,[])
        return output