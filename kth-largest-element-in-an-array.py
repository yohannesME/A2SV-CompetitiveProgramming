class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # left = 0
        # right = len(nums)-1

        def partition(left, right):
            pivot = right
            right -= 1


            while True:
                while left < pivot and nums[left] <= nums[pivot]:
                    left += 1

                while nums[right] > nums[pivot]:
                    right -= 1

                if right <= left:
                    break

                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            
            nums[left], nums[pivot] = nums[pivot], nums[left]
            return left
            
        def quickSelect(left, right):
            if right < left:
                return nums[N-k]
            
            pivot = partition(left, right)

            if pivot == N - k:
                return nums[pivot]
            elif pivot < N - k:
                return quickSelect(pivot+1, right)
            else:
                return quickSelect(left, pivot-1)
        

        # while True:
        #     if right < left:
        #         return nums[N - k]
        #     pivot = partition(left, right)
        #     if pivot == N-k:
        #         return nums[pivot]
        #     elif pivot < N - k:
        #         left = pivot + 1
        #     else:
        #         right = pivot - 1
        return quickSelect(0,N-1)