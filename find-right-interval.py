class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        indexHash = {}
        output = []
        N = len(intervals)

        for index, interval in enumerate(intervals):
            indexHash[(interval[0], interval[1])] = index

        sortedInterval = sorted(intervals)

        for starti, endi in intervals:
            left = 0
            right = N
            while left < right:
                mid = (left+right)//2

                if sortedInterval[mid][0] < endi:
                    left = mid + 1
                else:
                    right = mid

            if left < N and sortedInterval[left][0] >= endi:
                output.append(indexHash[(sortedInterval[left][0], sortedInterval[left][1])])
            else:
                output.append(-1)



        return output