# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         #iterating checkers
#         leftBound = 0
#         N = len(nums)
        
#         #iterate and check and even in the front and swap the accurance of even with it
#         while leftBound < N:
#             if nums[leftBound]%2 != 0:
#                 looker = leftBound
#                 while looker < N and nums[looker]%2 != 0:
#                     looker += 1
#                 if looker == N:
#                     break
#                 #swap the two occurances
#                 nums[looker], nums[leftBound] = nums[leftBound], nums[looker]

#             leftBound += 1
        
#         return nums

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #iterating checkers
        N = len(nums)
        leftBound = 0
        rightBound = N-1
        
        
        answer = [0]*N
        
        #iterate and check and even in the front and swap the accurance of even with it
        for num in nums:
            if num%2 == 0:
                answer[leftBound] = num
                leftBound += 1
            else:
                answer[rightBound] = num
                rightBound -= 1
        return answer
        
        return nums
                
