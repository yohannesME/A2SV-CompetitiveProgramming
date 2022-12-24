class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #iterating checkers
        leftBound = 0
        N = len(nums)
        
        #iterate and check and even in the front and swap the accurance of even with it
        while leftBound < N:
            if nums[leftBound]%2 != 0:
                looker = leftBound
                while looker < N and nums[looker]%2 != 0:
                    looker += 1
                if looker == N:
                    break
                #swap the two occurances
                nums[looker], nums[leftBound] = nums[leftBound], nums[looker]

            leftBound += 1
        
        return nums
                