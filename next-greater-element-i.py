class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N = len(nums1)
        greatest = [-1]*N
        indexHash = {}
        stack = []

        for index, num in enumerate(nums1):
            indexHash[num] = index

        for index in range(len(nums2)):
            while stack and stack[-1] < nums2[index]:
                greatest[indexHash[stack.pop()]] = nums2[index]
            
            if nums2[index] in indexHash:
                stack.append(nums2[index])

        return greatest