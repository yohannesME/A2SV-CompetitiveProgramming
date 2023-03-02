class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [-1]*N
        mStack = []
        
        #to create a simulation of the loop going circular we traverse through the  array twice
        #and add the index to mStack to keep track of the less elements and update it when we find a bigger one
        for index in range(N*2):
            while mStack and nums[mStack[-1]] < nums[index % N]:
                output[mStack.pop()] = nums[index % N]

            if index < N:
                mStack.append(index)

        return output