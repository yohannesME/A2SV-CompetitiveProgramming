class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subArray = 0
        lagging, fast = 0,0
        
        average = 0
        
        for i in  range(k):
            average += arr[fast]
            fast += 1
        fast -= 1
        while fast < len(arr):
            if ((average/k) >= threshold):
                subArray += 1
            average -= arr[lagging]
            lagging += 1
            fast += 1
            if fast < len(arr):
                average += arr[fast]
                
        return subArray
            
