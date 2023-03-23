class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        output = set()
        N = len(nums)

        #[] [4,5,6,7]
        #[4] [5,6,7]... this recursively calls until it exhaust every possible senario and adds it tothe set each time
        def backtrack(index, currentNums=()):
            if len(currentNums) > 1:
                output.add(currentNums)
            
            for i in range(index, N):
                if not currentNums or nums[i] >= currentNums[-1]:
                    backtrack(i+1, currentNums +tuple([nums[i]]))
        
        backtrack(0)

        return list(output)