class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prefix = [0]
        monoq = deque()

        #create a prefix sum of the nums
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        output = N+1

        for index, Pnum in enumerate(prefix):
            #we must keep an increasing monotonic queue so remove it does not abide by that rule
            while monoq and Pnum <= prefix[monoq[-1]]:
                monoq.pop()

            #if the range of prefix sum meaning that specific sub array sum is greater than k then update output and popleft from the queue
            while monoq and Pnum - prefix[monoq[0]] >= k:
                output = min(output, index-monoq.popleft())

            monoq.append(index)
        
        #check if output was never updated then return the answer
        return output if output != N+1 else -1