class Solution:
    def arraySortedOrNot(self, arr, n):
        prev = arr[0]
        for i in range(1, len(arr)):
            if prev > arr[i]:
                return False
                
            prev = arr[i]
        return True
