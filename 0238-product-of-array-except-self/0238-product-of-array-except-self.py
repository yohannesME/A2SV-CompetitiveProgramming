class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        #find the prefix and surfix for the product
        prefixFront = [1]
        for num in nums:
            prefixFront.append(prefixFront[-1]*num)
        
        prefixBack = [1]
        for index in range(N-1,-1,-1):
            prefixBack.append(prefixBack[-1]*nums[index])
        
        prefixBack.reverse()
        
        output = []
        
        #the output can be found by multiplying the surfix and prefix of that numbers current index
        for index in range(N):
            output.append(prefixFront[index]*prefixBack[index+1])
        
        return output