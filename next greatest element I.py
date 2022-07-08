class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greatest = []
        for i in range(len(nums1)):
            found = False
            added = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = True
                if found:
                    if nums1[i] < nums2[j]:
                        greatest.append(nums2[j])
                        added = True
                        break
            if not added:
                greatest.append(-1)
                

        return greatest
                    
        
