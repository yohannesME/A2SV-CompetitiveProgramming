class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        # found = True
        # while found:
        #     found = False
        #     for i in range(len(nums)-2,-1,-1):
        #         while nums[i] < nums[i+1]:
        #             nums[i] += 1
        #             nums[i+1] -= 1
        #             found = True
        #     print(nums)

        # return max(nums)

        left = sum(nums)//len(nums)
        right = max(nums)

        while left < right:
            mid = (left + right)//2
            numCopy = nums[:]

            for i in range(len(nums)-2,-1,-1):
                if numCopy[i+1] > mid:
                    add = numCopy[i+1] - mid
                    numCopy[i+1] = mid
                    numCopy[i] += add

            if max(numCopy) == mid:
                right = mid
            else:
                left = mid + 1
                
        return right