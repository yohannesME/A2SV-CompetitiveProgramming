class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #declaration of len and k
        k = -1
        N = len(nums)
        
        #move all the accurance of val to the right side
        for i in range(N):
            
            if nums[i] == val:
                looker = i
                k = i
                while looker < N and nums[looker] == val:
                    looker += 1
                
                if looker == N:
                    break
                
                #swap the the two instances
                nums[i], nums[looker] = nums[looker], nums[i]
        

        if k == -1:
            return N
        return k