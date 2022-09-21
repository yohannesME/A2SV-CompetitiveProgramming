class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def theFlip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        result = []
        for i in range(len(arr)-1, -1,-1):
            maxIndex = i
            for j in range(i, -1, -1):
                if (arr[j] > arr[maxIndex]): 
                    maxIndex = j
            if maxIndex != i:
                theFlip(maxIndex)
                theFlip(i)
                result.append(maxIndex+1)
                result.append(i+1)
        return result
                    
                    
