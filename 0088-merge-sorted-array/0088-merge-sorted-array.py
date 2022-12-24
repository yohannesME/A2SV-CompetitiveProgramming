class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #num1 bound tracker
        num1RightBound = n+m -1
        num1LeftBound = m-1
        
        #num2 bound trackers
        num2RightBound = n-1
        
        
        while num2RightBound > -1:
            #if num1 is done parsing just replace what is left with num2
            if num1LeftBound == -1:
                nums1[:num2RightBound+1] = nums2[:num2RightBound+1]
                break
                
            #if num2 is done parsing then just break the loop we are done
            if num2RightBound == -1:
                break
            
            if nums1[num1LeftBound] > nums2[num2RightBound]:
                nums1[num1RightBound] = nums1[num1LeftBound]
                num1LeftBound -= 1
            else:
                nums1[num1RightBound] = nums2[num2RightBound]
                num2RightBound -= 1
            
            num1RightBound -= 1

            