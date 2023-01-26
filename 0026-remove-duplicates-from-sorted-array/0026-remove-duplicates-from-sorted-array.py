class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #create a temp variable to store the last repeated value
        repeated = nums[0]
        N = len(nums)
        
        countRepeated = 1
        
        repeatedIndex = 1
        lookahead = 1
        
        while repeatedIndex < N and lookahead < N:
            while lookahead < N and nums[lookahead] == repeated:
                lookahead += 1
            
            if lookahead < N:
                countRepeated += 1
                nums[repeatedIndex] = nums[lookahead]
                repeatedIndex += 1
                repeated = nums[lookahead]
                
        
        return countRepeated
        