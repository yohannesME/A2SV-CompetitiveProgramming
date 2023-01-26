class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        N = len(nums)
        #if k is greater than size then return
        k = k%N
        
        #reverse the array to help us rotate
        nums.reverse()
        
        def reverseSubarray(leftBound,rightBound):
            while leftBound < rightBound:
                nums[leftBound],nums[rightBound] = nums[rightBound],nums[leftBound]
                leftBound += 1
                rightBound -= 1
        
        #then rotate the first k element and the rest alone
        leftBound = 0
        rightBound = k-1
        
        reverseSubarray(leftBound,rightBound)
        
        #then rotote the rest
        leftBound = k
        rightBound = N-1
        
        reverseSubarray(leftBound,rightBound)
        
        
        
