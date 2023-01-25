class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #create a num array that stores repeated value index
        repeatedNum = []
    
        #add the repeated value to num
        for i in range(0, len(nums)-1):
            if(nums[i]==nums[i+1]):
                repeatedNum.append(i)
            else:
                continue
        
        #pop the repeated element
        for i in range(len(repeatedNum)):
            #decrease by i as pop will decrease the array by one size
            nums.pop(repeatedNum[i]-i)
        
        return len(nums)
        