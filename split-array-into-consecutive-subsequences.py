class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heapArr = []

        nums = [-num for num  in nums]

        for num in nums:
            foundPlace = False

            for i in range(len(heapArr)-1, -1,-1):
                if num+1 == heapArr[i][0]:
                    heappush(heapArr[i], num)
                    foundPlace = True
                    break
            
            if not foundPlace:
                heapArr.append([num])

        for heap in heapArr:
            if len(heap) < 3:
                return False
        return True