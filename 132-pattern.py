class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        monoStack = []
        minvalue = float('inf')

        for index in range(len(nums)):
            while monoStack and monoStack[-1][0] <= nums[index]:
                monoStack.pop()

            if monoStack and monoStack[-1][1] < nums[index]:
                return True

            monoStack.append([nums[index], minvalue])
            minvalue = min(minvalue, nums[index])
        return False