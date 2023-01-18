class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #check the length of the array
        if len(arr) < 3:
            return False
            
        num = -1
        #mountain direction
        up = True
        for i in range(len(arr)-1):
            if arr[i+1] > arr[i] and up:
                pass
            if i == 0 and arr[i+1] < arr[i] and up:
                return False
            elif arr[i+1] < arr[i] and up:
                up = False
            elif arr[i+1] > arr[i] and not up:
                return False
            elif arr[i+1] == arr[i]:
                return False
                
        return True and not up