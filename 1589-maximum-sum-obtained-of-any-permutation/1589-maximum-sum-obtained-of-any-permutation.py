class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        N = len(nums)
        prefix = [0]*(N+1)
        
        maxReq = 0
        
        #get the request all together
        for start, end in requests:
            prefix[start] += 1
            prefix[end+1] -= 1
        
        #add them all up
        for i in range(1,N):
            prefix[i] += prefix[i-1]
        
        #remove the offset and sort them
        prefix.pop()
        prefix.sort()
        
        #add the maximum value * by maximum request
        for i in range(N):
            maxReq += prefix[i]*nums[i]
    
        return maxReq%(10**9+7)
        