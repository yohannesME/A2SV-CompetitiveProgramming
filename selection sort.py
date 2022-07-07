
class Solution: 
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minIndex = i
            for j in range(i,n):
                if(arr[minIndex] > arr[j]):
                    minIndex = j
            temp = arr[minIndex]
            arr[minIndex] = arr[i]
            arr[i] = temp
            
        return arr
