class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda inv: inv[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            finalEnd = result[-1][1]
            if start <= finalEnd:
                result[-1][1] = max(finalEnd, end)
            else:
                result.append([start, end])
        return result
