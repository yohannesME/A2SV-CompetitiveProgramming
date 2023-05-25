class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minimum = nums[0]
        twin = []

        for num in nums:
            if num > minimum:
                twin.append(num)
            minimum = min(minimum, num)
            
        if not twin:
            return False

        minimum = twin[0]
        for num in twin:
            if num > minimum:
                return True
            minimum = min(minimum, num)

        return False