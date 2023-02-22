class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]
        #create a prefix sum array with a offset one
        for num in nums:
            self.prefix.append(self.prefix[-1]+num)

    def sumRange(self, left: int, right: int) -> int:
        #keeping in mind the offset
        return self.prefix[right+1]-self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)