from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sortedPair = SortedList()
        pair = 0

        for num in nums:
            satisfyingRange = len(sortedPair) - bisect_left(sortedPair, num*2+1)
            
            if satisfyingRange > 0:
                pair +=  satisfyingRange

            sortedPair.add(num)

        return pair