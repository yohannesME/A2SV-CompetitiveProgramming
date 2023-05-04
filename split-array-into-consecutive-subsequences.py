class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heapArr = []

        for num in nums:
            foundPlace = False

            for i in range(len(heapArr)-1, -1,-1):
                if num-1 == heapArr[i][-1]:
                    heapArr[i].append(num)
                    foundPlace = True
                    break
            
            if not foundPlace:
                heapArr.append([num])

        return all(list(map(lambda x: len(x)>2, heapArr)))