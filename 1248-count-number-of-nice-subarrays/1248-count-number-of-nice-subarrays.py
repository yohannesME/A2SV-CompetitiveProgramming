class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #prepare a even and odd count 
        numsEvenCount = {}
        N = len(nums)
        
        for index in range(N):
            if nums[index] % 2 != 0:
                nums[index] = 1
            else:
                nums[index] = 0

        #add up the odd numbers
        prefixSum = [nums[0]]
        
        for index in range(1,N):
            prefixSum.append(prefixSum[-1]+nums[index])
        
        prefixHash = Counter(prefixSum)
        #the count of subarrays
        answer = 0
        
        #if the prefix count is there just add it else look for number of subarrays that will create that add
        for prefix in prefixSum:
            if prefix == k:
                answer += 1
            
            if prefix != 0:
                answer += prefixHash.get(prefix-k,0)

                
        return answer