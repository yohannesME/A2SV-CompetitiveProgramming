class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1,-1]
        N = len(nums)

        if not nums:
            return answer

        left = 0
        right = N-1

        while left < right:
            mid = (right+left)//2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if right >= N or nums[right] != target:
            return answer
        
        answer[0] = (right)

        left = 0
        right = N-1

        #biase the answer to the right
        while left < right:
            mid = (right+left)//2 + 1

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        answer[1] = (left)

        return answer