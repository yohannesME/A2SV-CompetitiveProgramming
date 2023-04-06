class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        #[maximum bit or, count of the maximum bit or]
        maximum = [0,0]

        def backtrack(mask=0, bitOr=0):
            #updat the maximum
            if bitOr > maximum[0]:
                maximum[0] = bitOr
                maximum[1] = 1
            elif bitOr == maximum[0]:
                maximum[1] += 1
            
            for i in range(len(nums)):
                if mask & (1 << i) == 0:
                    mask |= (1 << i)
                    backtrack(mask, bitOr|nums[i])

        
        backtrack()
        return maximum[1]