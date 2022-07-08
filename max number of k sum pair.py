class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        numbers = {}
        for i in range(len(nums)):
            if nums[i] > k:
                break
            else:
                numbers[nums[i]] = numbers.get(nums[i],0)+1
        count = 0
        for key in numbers:
            if abs(key-k) in numbers:
                count +=  min(numbers[key], numbers[abs(key-k)])

        return int(count/2)
        
