from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [0]*N
        sortedNums = SortedList()

        #traverse in a reverse order and bisect_left the sorted values to find the values lower than the value we desire.
        for i in range(N-1,-1,-1):
            output[i] = bisect_left(sortedNums, nums[i])
            sortedNums.add(nums[i])
        
        return output