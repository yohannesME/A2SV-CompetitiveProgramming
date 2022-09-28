class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        output = 0
        minq = collections.deque([])
        maxq = collections.deque([])
        
        start, end = 0,0
        
        while (end < len(nums)):
            endNum = nums[end]
            
            while(minq and nums[minq[-1]] > endNum):
                minq.pop()
            minq.append(end)
            
            while(maxq and nums[maxq[-1]] < endNum):
                maxq.pop()
            maxq.append(end)

            if(nums[maxq[0]] - nums[minq[0]] > limit):
                
                if nums[start] == nums[minq[0]]:
                    minq.popleft()
                if nums[start] == nums[maxq[0]]:
                    maxq.popleft()
                start += 1
            else:
                output = max(output, end-start+1)
            end += 1
        return output
    
