class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
    
        n = len(nums1)
        no_swap = [0] * n  
        swap = [1] * n  

        for i in range(1, n):
            no_swap[i] = swap[i] = n

            if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                no_swap[i] = no_swap[i - 1]
                swap[i] = swap[i - 1] + 1

            if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                no_swap[i] = min(no_swap[i], swap[i - 1])
                swap[i] = min(swap[i], no_swap[i - 1] + 1)

        return min(swap[n - 1], no_swap[n - 1])